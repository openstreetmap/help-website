+++
type = "question"
title = "overpass automatically set meta for dispatcher"
description = '''Hello everyone; I am trying to write a bash script to start and stop the dispatcher for overpass server to go with my  guide for setting up overpass in a Linux Slackware machine. You can see my guide here:  My database was initialed with meta data enabled, somebody else using my guide may not use me...'''
date = "2021-06-23T09:10:00Z"
lastmod = "2021-06-24T14:57:00Z"
weight = 80672
keywords = [ "overpass", "overpass-api" ]
aliases = [ "/questions/80672" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [overpass automatically set meta for dispatcher](/questions/80672/overpass-automatically-set-meta-for-dispatcher)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80672-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone;</p>
<p>I am trying to write a bash script to start and stop the dispatcher for overpass server to go with my guide for setting up overpass in a Linux Slackware machine. You can see my guide <a href="https://github.com/waelhammoudeh/overpass-4-slackware">here:</a></p>
<p>My database was initialed with meta data enabled, somebody else using my guide may not use meta data. Can I use the following test to automatically set "meta"?</p>
<pre><code>unset META
&#10;if [ -f ${DBDIR}/nodes_meta.bin ]; then
    META=--meta
fi</code></pre>
<p>DBDIR is database directory. Is testing for "nodes_meta.bin" file enough to set meta when starting dispatcher?</p>
<p>The complete script is below:</p>
<pre><code>#!/bin/bash
&#10;# script to start, stop and get status for overpass dispatcher daemon
# script is part of overpass slackbuild; it assumes installation into
# /usr/local directory and the creation of overpass user and group as
# indecated in the main README file included with the slackbuild script
#
# To use this script you need to set one varaible below:
# DBDIR : set it to your actual installation database directory.
#
&#10;DBDIR=/path/to/your/overpass/DBase
DSPTCHR=/usr/local/bin/dispatcher
SOCVER=v0.7.55
USER=overpass
unset META
&#10;if [ -f ${DBDIR}/nodes_meta.bin ]; then
    META=--meta
fi
&#10;if ! grep ^overpass: /etc/passwd 2&gt;&amp;1 &gt; /dev/null; then
&#10;    echo &quot;  You must have overpass user and group to run this script.&quot;
    echo &quot;   Please see the main \&quot;README\&quot; file included with build script&quot;
    exit 1
fi
&#10;# check dispatcher
if [ ! -x $DSPTCHR ]; then
&#10;    echo &quot;  Could not find dispatcher executable file!&quot;
    exit 2
fi
&#10;# test for database directory - directory can not be empty
if [ ! -d $DBDIR ]; then
&#10;    echo &quot; Could not find database directory&quot;
    exit 2
fi
&#10;# maybe nested if
if [ ! &quot;$(ls -A $DBDIR)&quot; ]; then
&#10;    echo &quot;  Seems like database directory is empty!&quot;
    echo &quot;  Please see \&quot;README.data\&quot; file included with build script.&quot;
    exit 2
fi
&#10;case &quot;$1&quot; in
&#10;    &quot;start&quot;)
&#10;    if (pgrep -f $DSPTCHR  2&gt;&amp;1 &gt; /dev/null) ; then
        echo &quot;dispatcher is already running!&quot;
        exit 0
&#10;    else
        echo &quot;dispatcher is NOT running&quot;
        if [ -S ${DBDIR}/osm3s_${SOCVER}_osm_base ]; then
            echo &quot;Found STALLED overpass socket file, removing.&quot;
            rm -f ${DBDIR}/osm3s_${SOCVER}_osm_base
        fi
    fi
&#10;    echo &quot;Starting overpass dispatcher ...&quot;
    sudo -u $USER $DSPTCHR --osm-base --db-dir=${DBDIR}/ ${META} &amp;
    sleep 1s
    if (! pgrep -f $DSPTCHR  2&gt;&amp;1 &gt; /dev/null) ; then
       echo &quot;Error: dispatcher did not start !!!&quot;
       exit 1
    else
        echo &quot;dispatcher started&quot;
    fi
&#10;    exit 0
;;
&#10;    &quot;stop&quot;)
&#10;        if (! pgrep -f $DSPTCHR  2&gt;&amp;1 &gt; /dev/null) ; then
            echo &quot;Error: dispatcher is not running.&quot;
            exit 2
        else
            sudo -u $USER $DSPTCHR --terminate
            sleep 1
            if (pgrep -f $DSPTCHR  2&gt;&amp;1 &gt; /dev/null) ; then
                echo &quot;Error: could not stop dispatcher&quot;
                exit 2
            else
                echo &quot;dispatcher stopped&quot;
            fi
        fi
        exit 0
;;
&#10;    &quot;status&quot;)
&#10;        if (pgrep -f $DSPTCHR  2&gt;&amp;1 &gt; /dev/null) ; then
            echo &quot;dispatcher is running&quot;
        else
            echo &quot;dispatcher is stopped&quot;
        fi
        echo &quot;&quot;
       sudo -u $USER $DSPTCHR --status
       exit 0
;;
&#10;    *)
        # something else - show usage
        echo &quot;&quot;
        echo &quot;  Error: Unkown command.&quot;
        echo &quot;  Usage: $0 ACTION&quot;
        echo &quot;  where ACTION is one of: { start, stop or status }&quot;
        echo &quot;&quot;
        echo &quot;  Please note they are all lower case letters!&quot;
        echo &quot;&quot;
        exit 1
    ;;
esac</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jun '21, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/88d38e1916b4f2210db71007b0b36b8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wael&#39;s gravatar image" />
<p><span>Wael</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wael has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80672" class="comments-container">
<span id="80690"></span>
<div id="comment-80690" class="comment">
<div id="post-80690-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This has nothing to do with Overpass. You'd be better off asking on one of the Stack Exchange forums.</p>
</div>
<div id="comment-80690-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 14:57)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-80672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80672-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

