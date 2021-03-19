+++
type = "question"
title = "SIP messages per user"
description = '''Hi folks, is there any possibility in Wireshark by using a special filter or a combination of some to show an overview of the number of SIP messages per user or endpoint? Trying to figure it out for SBC settings but with hundreds of thousands of IP endpoints you&#x27;re soon bored somehow. Greetz Marzen'''
date = "2013-08-14T08:19:00Z"
lastmod = "2013-08-20T02:44:00Z"
weight = 23772
keywords = [ "statistics", "sip", "endpoints" ]
aliases = [ "/questions/23772" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SIP messages per user](/questions/23772/sip-messages-per-user)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23772-score" class="post-score" title="current number of votes">0</div><span id="post-23772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks,</p><p>is there any possibility in Wireshark by using a special filter or a combination of some to show an overview of the number of SIP messages per user or endpoint? Trying to figure it out for SBC settings but with hundreds of thousands of IP endpoints you're soon bored somehow.</p><p>Greetz Marzen</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-endpoints" rel="tag" title="see questions tagged &#39;endpoints&#39;">endpoints</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '13, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/94fd46300ed34b55948adae577063490?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marzen&#39;s gravatar image" /><p><span>Marzen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marzen has no accepted answers">0%</span></p></div></div><div id="comments-container-23772" class="comments-container"></div><div id="comment-tools-23772" class="comment-tools"></div><div class="clear"></div><div id="comment-23772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23869"></span>

<div id="answer-container-23869" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23869-score" class="post-score" title="current number of votes">0</div><span id="post-23869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use tshark in conjunction with a perl/python script to extract the information you are interested in.</p><blockquote><p>tshark -nr sip.pcap -R "sip" -T fields -e frame.time -e ip.src -e ip.dst -e sip.from.addr -e sip.to.addr -e sip.Call-ID</p></blockquote><p>See the <a href="http://www.wireshark.org/docs/dfref/s/sip.html">SIP filter reference</a> for more fields.</p><p>Output (generated from a <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=MagicJack%2B_short_call.pcap">test file</a>):</p><pre><code>frame.time;ip.src;ip.dst;sip.from.addr;sip.to.addr;sip.Call-ID
Apr 12, 2012 17:40:15.711324000;192.168.0.10;216.234.64.8;sip:[email protected];sip:[email protected];C5570127C1A6A1ABF7ED9
DB9AD608CE00xc0a8000a
Apr 12, 2012 17:40:15.755652000;216.234.64.8;192.168.0.10;sip:[email protected];sip:[email protected];C5570127C1A6A1ABF7ED9
DB9AD608CE00xc0a8000a
Apr 12, 2012 17:40:15.769396000;216.234.64.8;192.168.0.10;sip:[email protected];sip:[email protected];C5570127C1A6A1ABF7ED9
DB9AD608CE00xc0a8000a
Apr 12, 2012 17:40:15.882668000;192.168.0.10;216.234.64.8;sip:[email protected];sip:[email protected];C5570127C1A6A1ABF7ED9
DB9AD608CE00xc0a8000a
Apr 12, 2012 17:40:15.884964000;192.168.0.10;216.234.64.8;sip:[email protected];sip:[email protected];C5570127C1A6A1ABF7ED9
DB9AD608CE00xc0a8000a
Apr 12, 2012 17:40:15.931983000;216.234.64.8;192.168.0.10;sip:[email protected];sip:[email protected];C5570127C1A6A1ABF7ED9
DB9AD608CE00xc0a8000a</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '13, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Aug '13, 02:53</strong> </span></p></div></div><div id="comments-container-23869" class="comments-container"></div><div id="comment-tools-23869" class="comment-tools"></div><div class="clear"></div><div id="comment-23869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

