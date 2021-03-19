+++
type = "question"
title = "Searching/Filtering Comments on packets in Pcap ng file"
description = '''I have added a few comments on a packet capture file in the Pcap NG format. Is there a way to filter/search for these comments? Thanks, Brian'''
date = "2012-11-29T06:46:00Z"
lastmod = "2015-03-09T01:33:00Z"
weight = 16420
keywords = [ "pcap", "comments", "ng" ]
aliases = [ "/questions/16420" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Searching/Filtering Comments on packets in Pcap ng file](/questions/16420/searchingfiltering-comments-on-packets-in-pcap-ng-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16420-score" class="post-score" title="current number of votes">0</div><span id="post-16420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have added a few comments on a packet capture file in the Pcap NG format. Is there a way to filter/search for these comments?</p><p>Thanks, Brian</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-comments" rel="tag" title="see questions tagged &#39;comments&#39;">comments</span> <span class="post-tag tag-link-ng" rel="tag" title="see questions tagged &#39;ng&#39;">ng</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '12, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/ca4d08b00778143dab07e2cde30f653c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brwiese&#39;s gravatar image" /><p><span>brwiese</span><br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brwiese has one accepted answer">50%</span></p></div></div><div id="comments-container-16420" class="comments-container"></div><div id="comment-tools-16420" class="comment-tools"></div><div class="clear"></div><div id="comment-16420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="16633"></span>

<div id="answer-container-16633" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16633-score" class="post-score" title="current number of votes">1</div><span id="post-16633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The best way in Wireshark is to use a display filter like this one:</p><pre><code>pkt_comment contains &quot;searchString&quot;</code></pre><p>If you prefer command line then I'd recommend tshark + grep:</p><pre><code>tshark -r dump.pcapng -T fields -e pkt_comment -R pkt_comment | grep SearchString</code></pre><p>Please see the blog post <a href="http://netresec.com/?b=12CB2A2">HowTo handle PcapNG files</a> for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '12, 05:05</strong></p><img src="https://secure.gravatar.com/avatar/0b454840884fddcd9c080d5e05608633?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Netresec&#39;s gravatar image" /><p><span>Netresec</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Netresec has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Dec '12, 05:07</strong> </span></p></div></div><div id="comments-container-16633" class="comments-container"></div><div id="comment-tools-16633" class="comment-tools"></div><div class="clear"></div><div id="comment-16633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16421"></span>

<div id="answer-container-16421" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16421-score" class="post-score" title="current number of votes">0</div><span id="post-16421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the search function.</p><blockquote><p><code>Edit -&gt; Find Packet</code><br />
</p></blockquote><p>Select these options:</p><ul><li>String</li><li>packet details</li></ul><p>The other option is a Display Filter:</p><blockquote><p><code>frame.comment contains "Your string"</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '12, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Nov '12, 06:54</strong> </span></p></div></div><div id="comments-container-16421" class="comments-container"><span id="16424"></span><div id="comment-16424" class="comment"><div id="post-16424-score" class="comment-score"></div><div class="comment-text"><p>Or use the filter "pkt_comment" or "frame.comment" or "frame.comment=="My comment".</p><p>The last one may be tricky as I think it includes \a \n etc.</p></div><div id="comment-16424-info" class="comment-info"><span class="comment-age">(29 Nov '12, 07:07)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="16432"></span><div id="comment-16432" class="comment"><div id="post-16432-score" class="comment-score"></div><div class="comment-text"><p>Or add a custom column with the "frame.comment" setting as column value. This might not be useful for large file with only a few scattered comments though.</p></div><div id="comment-16432-info" class="comment-info"><span class="comment-age">(29 Nov '12, 09:13)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-16421" class="comment-tools"></div><div class="clear"></div><div id="comment-16421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40376"></span>

<div id="answer-container-40376" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40376-score" class="post-score" title="current number of votes">0</div><span id="post-40376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I found pkt_comment contains "searchString" does not work, but frame.comment contains "Your string" works.</p><p>Not know why.</p><p>The wireshark version is Version 1.12.3 (v1.12.3-0-gbb3e9a0 from master-1.12).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '15, 01:33</strong></p><img src="https://secure.gravatar.com/avatar/cd85c037495c85c4d3e6feb898db5207?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuguang&#39;s gravatar image" /><p><span>yuguang</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuguang has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-40376" class="comments-container"></div><div id="comment-tools-40376" class="comment-tools"></div><div class="clear"></div><div id="comment-40376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

