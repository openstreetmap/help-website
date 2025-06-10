+++
type = "question"
title = "Problem to compile extractor.cpp OSRM"
description = '''Hello everybody, I am trying to compile extractor.cpp but It doesn&#x27;t work... The error message is: *In file included from extractor.cpp:32:0: Extractor/XMLParser.h:37:30: fatal error: libxml/xmlreader.h: File o directory non esistente compilation terminated.*  I don&#x27;t understand why, I have just fol...'''
date = "2014-02-07T14:19:00Z"
lastmod = "2014-02-11T07:45:00Z"
weight = 30536
keywords = [ "osrm", "extract" ]
aliases = [ "/questions/30536" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem to compile extractor.cpp OSRM](/questions/30536/problem-to-compile-extractorcpp-osrm)

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
<span id="post-30536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30536-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everybody, I am trying to compile extractor.cpp but It doesn't work... The error message is:</p>
<pre><code>*In file included from extractor.cpp:32:0:
Extractor/XMLParser.h:37:30: fatal error: libxml/xmlreader.h: File o directory non esistente
compilation terminated.*</code></pre>
<p>I don't understand why, I have just follow the github at this <a href="https://github.com/DennisOSRM/Project-OSRM/wiki/Building%20OSRM">page</a></p>
<p>and I have install the package for ubuntu 12.04... Can someone help me? To compile I use in the shell this command: g++ -Wall -W -Werror extractor.cpp -o extract</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Feb '14, 14:19</strong></p>
<img src="https://secure.gravatar.com/avatar/3be508f311801a447f51a4dab36a0e57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoifil&#39;s gravatar image" />
<p><span>Zoifil</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoifil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30536" class="comments-container">
<span id="30545"></span>
<div id="comment-30545" class="comment">
<div id="post-30545-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>did you follow the instructions at this section? <a href="https://github.com/DennisOSRM/Project-OSRM/wiki/Building%20OSRM#wiki-ubuntu-1204">https://github.com/DennisOSRM/Project-OSRM/wiki/Building%20OSRM#wiki-ubuntu-1204</a> note that unless you are copying and pasting, when there is a <code>\</code>, ignore it and keep typing the next line without pressing <code>Enter</code></p>
</div>
<div id="comment-30545-info" class="comment-info">
<span class="comment-age">(07 Feb '14, 17:38)</span> <span class="comment-user userinfo">jgpacker</span>
</div>
</div>
<span id="30554"></span>
<div id="comment-30554" class="comment">
<div id="post-30554-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does installing <code>libxml2-dev</code> resolve the issue?</p>
</div>
<div id="comment-30554-info" class="comment-info">
<span class="comment-age">(08 Feb '14, 09:59)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="30584"></span>
<div id="comment-30584" class="comment">
<div id="post-30584-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes yes, I have already follow and do the instruction for ubuntu 12,04 and all of the packet are already install...</p>
</div>
<div id="comment-30584-info" class="comment-info">
<span class="comment-age">(10 Feb '14, 11:10)</span> <span class="comment-user userinfo">Zoifil</span>
</div>
</div>
<span id="30592"></span>
<div id="comment-30592" class="comment">
<div id="post-30592-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But <code>libxml2-dev</code> does <a href="http://packages.ubuntu.com/precise/amd64/libxml2-dev/filelist">contain libxml/xmlreader.h</a>. Please check if <em>/usr/include/libxml2/libxml/xmlreader.h</em> exists.</p>
</div>
<div id="comment-30592-info" class="comment-info">
<span class="comment-age">(10 Feb '14, 17:56)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="30618"></span>
<div id="comment-30618" class="comment">
<div id="post-30618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes there is...for my opininion the problem is that I have install all the packages and I also have install lua 5.1 and after I have disinstall all the lua packages... and so I have already install all...</p>
</div>
<div id="comment-30618-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 07:45)</span> <span class="comment-user userinfo">Zoifil</span>
</div>
</div>
</div>
<div id="comment-tools-30536" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30536-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

