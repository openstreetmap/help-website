+++
type = "question"
title = "Filtering specific IP"
description = '''I am new to wireshark and would like to know the easiest way of Filtering all traffic coming and going from a specific IP address on out network. any help would be greatly appreciated.'''
date = "2012-11-29T13:34:00Z"
lastmod = "2012-11-30T10:51:00Z"
weight = 16439
keywords = [ "filtering" ]
aliases = [ "/questions/16439" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering specific IP](/questions/16439/filtering-specific-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16439-score" class="post-score" title="current number of votes">1</div><span id="post-16439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to wireshark and would like to know the easiest way of Filtering all traffic coming and going from a specific IP address on out network. any help would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '12, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/3676525ee4b1b8a4f8fa779e860d9695?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ksimpson&#39;s gravatar image" /><p><span>ksimpson</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ksimpson has no accepted answers">0%</span></p></div></div><div id="comments-container-16439" class="comments-container"></div><div id="comment-tools-16439" class="comment-tools"></div><div class="clear"></div><div id="comment-16439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16440"></span>

<div id="answer-container-16440" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16440-score" class="post-score" title="current number of votes">2</div><span id="post-16440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use a <a href="http://wiki.wireshark.org/CaptureFilters">capture filter</a></p><blockquote><p><code>host 10.10.10.1</code><br />
</p></blockquote><p>or a <a href="http://wiki.wireshark.org/DisplayFilters">display filter</a></p><blockquote><p><code>ip.addr == 10.10.10.1</code><br />
</p></blockquote><p>You'll find general information about Wiresahrk in the Wiki.</p><blockquote><p><code>http://wiki.wireshark.org/</code><br />
</p></blockquote><p>The following videos might also be interesting:</p><blockquote><p><code>http://www.youtube.com/watch?v=pk4OfsxxB4g&amp;feature=related</code><br />
<code>http://www.youtube.com/watch?v=NHLTa29iovU</code><br />
<code>http://wiresharkdownloads.riverbed.com/video/wireshark/introduction-to-wireshark/</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '12, 13:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Nov '12, 13:57</strong> </span></p></div></div><div id="comments-container-16440" class="comments-container"><span id="16441"></span><div id="comment-16441" class="comment"><div id="post-16441-score" class="comment-score"></div><div class="comment-text"><p>I have tried that and I am still getting everything not that one specific IP.</p></div><div id="comment-16441-info" class="comment-info"><span class="comment-age">(29 Nov '12, 14:00)</span> <span class="comment-user userinfo">ksimpson</span></div></div><span id="16443"></span><div id="comment-16443" class="comment"><div id="post-16443-score" class="comment-score"></div><div class="comment-text"><p>what exactly did you try?</p></div><div id="comment-16443-info" class="comment-info"><span class="comment-age">(29 Nov '12, 15:50)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16469"></span><div id="comment-16469" class="comment"><div id="post-16469-score" class="comment-score"></div><div class="comment-text"><p>the capture filter then the display filter, I did install wireshark on another machine and got the capture filter to work except it is only showing information from the same vlan as the machine i am wanting to watch.</p></div><div id="comment-16469-info" class="comment-info"><span class="comment-age">(30 Nov '12, 09:13)</span> <span class="comment-user userinfo">ksimpson</span></div></div><span id="16470"></span><div id="comment-16470" class="comment"><div id="post-16470-score" class="comment-score"></div><div class="comment-text"><blockquote><p>only showing information from the same vlan as the machine i am wanting to watch.</p></blockquote><p>well, that's normal, as you need to setup a proper capturing environment to see traffic of other VLANs and/or other systems.</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Ethernet</code><br />
</p></blockquote><p>Basically you need to configure port mirroring on your switch (see link above).</p></div><div id="comment-16470-info" class="comment-info"><span class="comment-age">(30 Nov '12, 10:51)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-16440" class="comment-tools"></div><div class="clear"></div><div id="comment-16440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

