+++
type = "question"
title = "Question about Filter the SIP by tshark"
description = '''I want to get all sip message in .pcap file. I use &quot;&quot;tshark -r c:&#92;a.pcap -Y sip -z &quot;sip,stat,ip.addr==10.10.10.3&quot; -w a.txt&quot;&quot; But the out put will like  ?  h 5? ??H H Cv w蝴皝? E :P| 璦+??&amp;amp;踦SIP/2.0 100 Trying Via: SIP/2.0/UDP 10.10.10.43;rport=5060;branch=z9hG4bK+PhOpZMrrpHouo From: &quot;7000&quot;...'''
date = "2014-08-12T23:08:00Z"
lastmod = "2014-08-17T22:39:00Z"
weight = 35448
keywords = [ "sip", "tshark" ]
aliases = [ "/questions/35448" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Question about Filter the SIP by tshark](/questions/35448/question-about-filter-the-sip-by-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35448-score" class="post-score" title="current number of votes">0</div><span id="post-35448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to get all sip message in .pcap file.</p><p>I use ""tshark -r c:\a.pcap -Y sip -z "sip,stat,ip.addr==10.10.10.3" -w a.txt""</p><p>But the out put will like</p><p>?  h 5? ??H H Cv w蝴皝? E :P| €璦+??&amp;踦SIP/2.0 100 Trying</p><p>Via: SIP/2.0/UDP 10.10.10.43;rport=5060;branch=z9hG4bK+PhOpZMrrpHouo</p><p>From: "7000" <span>sip:<span class="__cf_email__" data-cfemail="af989f9f9fef9e9f819e9f819e9f819c">[email protected]</span></span>;tag=Qklz17s+TogPIm</p><p>It will have some broken message.</p><p>I want all the out put like shown:</p><p>INVITE <span class="__cf_email__" data-cfemail="b7d4d6dbdbd2d3f7dfdedac48599d9d2c3">[email protected]</span> SIP/2.0,</p><p>P-Preferred-Identity: <span class="__cf_email__" data-cfemail="c9aaa8a5a5acbb89a1a0a4baf8e7a7acbd">[email protected]</span>,</p><p>Via: Calling UE IP :Port,</p><p>Route: P-CSCF address,</p><p>Route: S-CSCF address,</p><p>Contact: Calling UE IP :Port,</p><p>SDP: Caller Supported Codec List</p><p>can some one tell me how to set the tshark parameter?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '14, 23:08</strong></p><img src="https://secure.gravatar.com/avatar/6610a4c7ccdab2fe25d3fe121baca552?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grayyoung&#39;s gravatar image" /><p><span>grayyoung</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grayyoung has no accepted answers">0%</span></p></div></div><div id="comments-container-35448" class="comments-container"></div><div id="comment-tools-35448" class="comment-tools"></div><div class="clear"></div><div id="comment-35448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35450"></span>

<div id="answer-container-35450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35450-score" class="post-score" title="current number of votes">1</div><span id="post-35450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>tshark -r c:\a.pcap -Y sip -z "sip,stat,ip.addr==10.10.10.3" -w a.txt</p></blockquote><p><strong>-w a.txt</strong> will write a <strong>pcap</strong> file of the filtered frames! If you want the text output of <strong>-z "sip,stat"</strong> you should run tshark like this.</p><blockquote><p>tshark -r c:\a.pcap -Y sip -z "sip,stat,ip.addr==10.10.10.3" &gt; a.txt</p></blockquote><pre><code>===================================================================
SIP Statistics with filter ip.addr==x.x.x.x

Number of SIP messages: 10
Number of resent SIP messages: 0

* SIP Status Codes in reply packets
  SIP 180 Ringing         :     2 Packets
  SIP 200 OK              :     2 Packets
  SIP 100 Trying          :     2 Packets

* List of SIP Request methods
  INVITE          :     2 Packets
  ACK             :     1 Packets
  REGISTER        :     1 Packets

* Average setup time 8525 ms
 Min 8525 ms
 Max 8525 ms
===================================================================</code></pre><p><strong>However</strong>, that gives only <strong>statistics</strong>, not the whole SIP call flow!! If you need that, please add a comment.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '14, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35450" class="comments-container"><span id="35499"></span><div id="comment-35499" class="comment"><div id="post-35499-score" class="comment-score"></div><div class="comment-text"><p>Yes I know this method, but I need the SIP and SDP format,</p><p>If I use the parameter -V,</p><p>That will have to much information,</p><p>is there any parameter can filter only sip header, SDP?</p></div><div id="comment-35499-info" class="comment-info"><span class="comment-age">(14 Aug '14, 23:20)</span> <span class="comment-user userinfo">grayyoung</span></div></div><span id="35505"></span><div id="comment-35505" class="comment"><div id="post-35505-score" class="comment-score"></div><div class="comment-text"><p>can you please show an example of what exactly you want to get?</p></div><div id="comment-35505-info" class="comment-info"><span class="comment-age">(15 Aug '14, 09:00)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="35522"></span><div id="comment-35522" class="comment"><div id="post-35522-score" class="comment-score"></div><div class="comment-text"><p>Actually, I want to build the XML file for replay the communication of UE and server.</p><p>So I need SIP(all header), SDP，</p><p>and I still try to know how to get the RTP from tshark,</p><p>and how I can combine them all.</p></div><div id="comment-35522-info" class="comment-info"><span class="comment-age">(17 Aug '14, 22:39)</span> <span class="comment-user userinfo">grayyoung</span></div></div></div><div id="comment-tools-35450" class="comment-tools"></div><div class="clear"></div><div id="comment-35450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

