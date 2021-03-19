+++
type = "question"
title = "Form Snmptrap command from Wireshark capture"
description = '''Hey guys, I was hunting forum posts to see if something similar was ever asked and did not find it already... I am working to reproduce an issue in my monitoring system and to do so, it would greatly help if I could use snmptrap to send an identical trap as the device I&#x27;m troubleshooting.  I wanted ...'''
date = "2014-06-10T14:39:00Z"
lastmod = "2014-06-19T14:21:00Z"
weight = 33629
keywords = [ "snmptrap" ]
aliases = [ "/questions/33629" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Form Snmptrap command from Wireshark capture](/questions/33629/form-snmptrap-command-from-wireshark-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33629-score" class="post-score" title="current number of votes">0</div><span id="post-33629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys, I was hunting forum posts to see if something similar was ever asked and did not find it already...</p><p>I am working to reproduce an issue in my monitoring system and to do so, it would greatly help if I could use snmptrap to send an identical trap as the device I'm troubleshooting.<br />
</p><p>I wanted to ask and see if there was already an easy to follow guide that explains how to read the capture from wireshark and formulate a snmptrap command to mimic the trap.</p><p>I am rather green with wireshark and snmptrap so any advice is appreciative.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-snmptrap" rel="tag" title="see questions tagged &#39;snmptrap&#39;">snmptrap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '14, 14:39</strong></p><img src="https://secure.gravatar.com/avatar/5f5f62c8e2b5f1d6dc5ac893b1f9d344?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BenB&#39;s gravatar image" /><p><span>BenB</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BenB has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-33629" class="comments-container"></div><div id="comment-tools-33629" class="comment-tools"></div><div class="clear"></div><div id="comment-33629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33711"></span>

<div id="answer-container-33711" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33711-score" class="post-score" title="current number of votes">1</div><span id="post-33711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>it would work for SNMP v1 and v2 traps, however not for v3 traps (due to the authentication). So, here is how I would do it. I can't write the whole script for you, as that's quite some work...</p><p><strong>First</strong> 'print' the content of SNMP trap frames with tshark and pipe the output into your script (you'll have to write that!).</p><blockquote><p>tshark -nr input-snmpv1-trap.pcap -Y "snmp.trap" -V | yourscript.pl</p></blockquote><p>Result of tshark:</p><pre><code>User Datagram Protocol, Src Port: 1040 (1040), Dst Port: 162 (162)
    Source port: 1040 (1040)
    Destination port: 162 (162)
    Length: 66
    Checksum: 0x823c [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
Simple Network Management Protocol
    version: version-1 (0)
    community: public
    data: trap (4)
        trap
            enterprise: 1.3.6.1.4.1.4.1.2.21 (iso.3.6.1.4.1.4.1.2.21)
            agent-addr: 127.0.0.1 (127.0.0.1)
            generic-trap: coldStart (0)
            specific-trap: 0
            time-stamp: 0
            variable-bindings: 1 item
                1.3.6.1.2.1.2.1.0: 
                    Object Name: 1.3.6.1.2.1.2.1.0 (iso.3.6.1.2.1.2.1.0)
                    Value (Integer32): 33</code></pre><p><strong>Second:</strong> Within your script, look for the SNMP 'parameters' to form the <a href="http://www.net-snmp.org/docs/man/snmptrap.html">snmptrap</a> command, which are (just some examples)</p><blockquote><p>version: version-1 (0)<br />
community: public<br />
Object Name: 1.3.6.1.2.1.2.1.0 (iso.3.6.1.2.1.2.1.0) Value (Integer32): 33</p></blockquote><p>Unfortunately SNMPv1 traps look differently than SNMPv2 traps and the same holds true for the <a href="http://www.net-snmp.org/docs/man/snmptrap.html">snmptrap</a> commands (see the man page). Furthermore there are several value types (int32, etc.) which you'll have to translate to snmptrap parameters.</p><p>Result: Yes, it's possible to create a <a href="http://www.net-snmp.org/docs/man/snmptrap.html">snmptrap</a> command based on the capture file, but the script that parses the tshark output has to do 'some work' to make it happen.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '14, 06:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-33711" class="comments-container"><span id="33967"></span><div id="comment-33967" class="comment"><div id="post-33967-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt! This was extremely helpful, I'll get to writing the script, and then post my results.</p></div><div id="comment-33967-info" class="comment-info"><span class="comment-age">(19 Jun '14, 14:21)</span> <span class="comment-user userinfo">BenB</span></div></div></div><div id="comment-tools-33711" class="comment-tools"></div><div class="clear"></div><div id="comment-33711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

