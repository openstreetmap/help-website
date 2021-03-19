+++
type = "question"
title = "TShark Command for Capturing only TCP SYN Packets?"
description = '''Hi Everyone, I&#x27;m attempting to baseline my network&#x27;s typical SYN Requests sourced from the internet. Our organization was recently DDoS&#x27;d with a SYN Flood and my goal here is to find out what typical SYN traffic looks like so I can create a threshold on our firewall to prevent another SYN Flood atta...'''
date = "2017-04-07T13:37:00Z"
lastmod = "2017-04-07T16:32:00Z"
weight = 60662
keywords = [ "elk", "ddos", "tshark", "syn" ]
aliases = [ "/questions/60662" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TShark Command for Capturing only TCP SYN Packets?](/questions/60662/tshark-command-for-capturing-only-tcp-syn-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60662-score" class="post-score" title="current number of votes">0</div><span id="post-60662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Everyone,</p><p>I'm attempting to baseline my network's typical SYN Requests sourced from the internet. Our organization was recently DDoS'd with a SYN Flood and my goal here is to find out what typical SYN traffic looks like so I can create a threshold on our firewall to prevent another SYN Flood attack without this configuration being detrimental to legitimate traffic.</p><p>My idea is to use TShark to do an ongoing capture starting a new file every 60 seconds the grabbing Time, Source IP, and Destination IP of <strong>ONLY</strong> SYN Requests sourced from the internet (anything NOT in RFC 1918 Subnets). Then, pump that data into a .csv so I can send it to my ELK Stack for analysis.</p><p>I am pretty unfamiliar with TShark as I typicaly use Wireshark GUI. I found something similar to what I'm looking for here</p><pre><code>https://rudibroekhuizen.wordpress.com/2016/02/12/analyse-tshark-capture-in-kibana/</code></pre><p>but I'm not quite sure how to write out what I need.</p><p>Can anyone offer some help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-elk" rel="tag" title="see questions tagged &#39;elk&#39;">elk</span> <span class="post-tag tag-link-ddos" rel="tag" title="see questions tagged &#39;ddos&#39;">ddos</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '17, 13:37</strong></p><img src="https://secure.gravatar.com/avatar/6b5561becebc6b21148e4a191a63c924?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Exiar&#39;s gravatar image" /><p><span>Exiar</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Exiar has no accepted answers">0%</span></p></div></div><div id="comments-container-60662" class="comments-container"></div><div id="comment-tools-60662" class="comment-tools"></div><div class="clear"></div><div id="comment-60662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60663"></span>

<div id="answer-container-60663" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60663-score" class="post-score" title="current number of votes">1</div><span id="post-60663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Using tshark in this manner you'll need to specify a few things, noting that if you want to create a new file every 60 seconds you'll have to output using a capture file format, e.g. pcapng and then subsequently post-process those using tshark to output in csv format, you can't just redirect tshark "fields" out and get multiple files, the link you reference is a one-shot run of 60 seconds:</p><ol><li>The interface(s) to capture on, e.g. <code>-i eth0</code></li><li>The capture file options, for a new file every 60 seconds use <code>-b duration:60</code></li><li>The output file, for ringbuffer use <code>-w basefilename.pcapng</code>, each new file created will add a suffix to the basename</li><li>The capture filter, something like <code>"tcp[tcpflags] &amp; (tcp-syn) == tcp-syn and not (src net (10 or 172.16/12 or 192.168/16) and dst net (10 or 172.16/12 or 192.168/16))"</code>. You may or may not need to quote this depending on your shell.</li></ol><p>Then post-process those files with something like <code>tshark -r filename.pcapng -T fields -e frame.time -e ip.src -e ip.dst &gt; filename.csv</code> using the scripting language of choice to loop over all the files providing the "filename" part of the command.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '17, 16:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Apr '17, 11:16</strong> </span></p></div></div><div id="comments-container-60663" class="comments-container"></div><div id="comment-tools-60663" class="comment-tools"></div><div class="clear"></div><div id="comment-60663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

