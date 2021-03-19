+++
type = "question"
title = "voip tshark capture"
description = '''Hello guys, I need to capture voip calls from asterisk with tshark command and send to a file to later listen the calls, like Telephony -&amp;gt; VoIP Calls, do. It is possible do this task with tshark, without GUI interface of wireshark installed? Thanks in advance'''
date = "2015-08-13T20:04:00Z"
lastmod = "2015-08-14T06:19:00Z"
weight = 45086
keywords = [ "voip" ]
aliases = [ "/questions/45086" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [voip tshark capture](/questions/45086/voip-tshark-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45086-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys,</p><p>I need to capture voip calls from asterisk with tshark command and send to a file to later listen the calls, like Telephony -&gt; VoIP Calls, do.</p><p>It is possible do this task with tshark, without GUI interface of wireshark installed?</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '15, 20:04</strong></p><img src="https://secure.gravatar.com/avatar/559b970f73d0da249f79452fe3f9b2c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="luis_filipe&#39;s gravatar image" /><p>luis_filipe<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="luis_filipe has no accepted answers">0%</span></p></div></div><div id="comments-container-45086" class="comments-container"></div><div id="comment-tools-45086" class="comment-tools"></div><div class="clear"></div><div id="comment-45086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45092"></span>

<div id="answer-container-45092" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45092-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>you can use tcpdump for example :)</p><p>try this init.d script.But first make changes</p><ul><li>eth1 (network interface)</li><li>tcp portrange 1720-1725 or udp portrange 5060-5065 (signaling portrange of your server)</li><li>tcp portrange 1720-1725 or udp portrange (5060-5065 or 10000-29999) (signaling and media-rtp portrange of your server)</li></ul><p>What this script do:</p><ol><li>Check if scrip already run - if yes - stop.</li><li>Create subfolder if not exist in <strong>DUMPDIR</strong> folder name will be like <em>YearMonthDay - 20150814</em>.</li><li>Making continius logging in <strong>pcap</strong> during all time script working. Logs divided by 1 hour period file with name like <em>dump_Year-Month-Day_HourMinuteSecond - dump_2015-08-14_102201</em>.</li><li>Compress each file by gzip after end of work with them.</li><li>Create different logs for signaling OR signaling+media data.</li></ol><pre><code>#!/bin/bash

#
#Use this comand
#tcpdump -n -vvv SOME_FILTER -r ./SOME.pcap -w RESULT_FILE.pcap
#for cutting
#

test -x /usr/sbin/tcpdump || exit 0
start(){
    RETVAL=0
    PIDDUMP=/var/run/tcpdump_dump.pid
    PIDSIG=/var/run/tcpdump_sig.pid

    TODAY=`date +%Y%m%d`
    DUMPDIR=&quot;/home/myuser/DUMP/${TODAY}&quot;

    if [ -f $PIDDUMP ]; then
        echo &quot;PID DUMP is exist stop it first&quot;
        RETVAL=1
    fi

    if [ -f $PIDSIG ]; then
    echo &quot;PID SIG is exist stop it first&quot;
    RETVAL=1
    fi

    if [ $RETVAL -eq 0 ];then

    if [ ! -d $DUMPDIR ]; then
        mkdir $DUMPDIR
        fi

        echo &quot;Starting tcpdump&quot;

    /usr/sbin/tcpdump -s0 -w - -i eth1 tcp portrange 1720-1725 or udp portrange 5060-5065 -G 3600 -w &quot;${DUMPDIR}/sign_%Y-%m-%d_%H%M%S.pcap&quot; -z gzip &amp;
    echo $! &gt; $PIDSIG

    /usr/sbin/tcpdump -s0 -w - -i eth1 tcp portrange 1720-1725 or udp portrange \(5060-5065 or 10000-29999\) -G 3600 -w &quot;${DUMPDIR}/dump_%Y-%m-%d_%H%M%S.pcap&quot; -z gzip &amp;
    echo $! &gt; $PIDDUMP
    fi

    exit $RETVAL
}

stop () {
      # stop daemon
    echo &quot;Stopping tcpdump&quot;
    PIDDUMP=/var/run/tcpdump_dump.pid
    PIDSIG=/var/run/tcpdump_sig.pid
        if [ -f $PIDDUMP ]; then
          kill $(cat $PIDDUMP)
          rm $PIDDUMP
        else
          echo &quot;PID DUMP does not exist&quot;
        fi

        if [ -f $PIDSIG ]; then
          kill $(cat $PIDSIG)
          rm $PIDSIG
        else
          echo &quot;PID SIG does not exist&quot;
        fi
    return $RETVAL
 }

 restart () {
     stop
     start
     RETVAL=$?
     return $RETVAL
 }

 case &quot;$1&quot; in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    *)
        echo &quot;Usage: $0 {start|stop|restart}&quot;
        RETVAL=1
 esac

 exit $RETVAL</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '15, 00:31</strong></p><img src="https://secure.gravatar.com/avatar/0319823751d2656828f8f21f22b90b05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sindar&#39;s gravatar image" /><p>Sindar<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sindar has no accepted answers">0%</span></p></div></div><div id="comments-container-45092" class="comments-container"><span id="45106"></span><div id="comment-45106" class="comment"><div id="post-45106-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the script, but my question was about tshark not tcpdump, ok</p><p>I can not install anything on the server and only have available the tshark , understand?</p></div><div id="comment-45106-info" class="comment-info"><span class="comment-age">(14 Aug '15, 05:12)</span> luis_filipe</div></div></div><div id="comment-tools-45092" class="comment-tools"></div><div class="clear"></div><div id="comment-45092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45107"></span>

<div id="answer-container-45107" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45107-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Capture yes, extracting the VoIP calls no. For capture you should probably use the dumpcap utility i.s.o. tshark (if you have tshark and you can capture then you have that already installed). You could even convert the script given in another answer to use dumpcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '15, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-45107" class="comments-container"></div><div id="comment-tools-45107" class="comment-tools"></div><div class="clear"></div><div id="comment-45107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

