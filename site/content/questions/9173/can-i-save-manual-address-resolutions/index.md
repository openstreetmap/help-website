+++
type = "question"
title = "Can I save manual address resolutions?"
description = '''Is there any way to SAVE manually resolved addresses to LOAD them next time Wireshark runs?'''
date = "2012-02-22T09:21:00Z"
lastmod = "2012-02-24T06:35:00Z"
weight = 9173
keywords = [ "ip", "resolve", "address" ]
aliases = [ "/questions/9173" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I save manual address resolutions?](/questions/9173/can-i-save-manual-address-resolutions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9173-score" class="post-score" title="current number of votes">0</div><span id="post-9173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way to SAVE manually resolved addresses to LOAD them next time Wireshark runs?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-resolve" rel="tag" title="see questions tagged &#39;resolve&#39;">resolve</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '12, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/c241cfce7680c690b68422163a98c0d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="contradictor_&#39;s gravatar image" /><p><span>contradictor_</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="contradictor_ has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Feb '12, 17:18</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-9173" class="comments-container"></div><div id="comment-tools-9173" class="comment-tools"></div><div class="clear"></div><div id="comment-9173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9186"></span>

<div id="answer-container-9186" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9186-score" class="post-score" title="current number of votes">2</div><span id="post-9186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can create a hosts file and put it in the Wireshark configuration directory. This file follows the same format as the standard Windows or UNIX hosts file. Wireshark will read this file at startup and will use it as long as network name resolution is enabled.</p><p>Note that Wireshark will only read this file at startup, so if you make changes while Wireshark is running, you will need to shut down Wireshark and restart for the changes to take effect.</p><p>See <a href="http://wiki.wireshark.org/Preferences/NameResolution">Preferences/Name Resolution</a> on the Wireshark Wiki.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '12, 10:57</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Feb '12, 11:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-9186" class="comments-container"></div><div id="comment-tools-9186" class="comment-tools"></div><div class="clear"></div><div id="comment-9186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9175"></span>

<div id="answer-container-9175" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9175-score" class="post-score" title="current number of votes">0</div><span id="post-9175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With the development version using pcap-ng file format - yes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '12, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-9175" class="comments-container"><span id="9181"></span><div id="comment-9181" class="comment"><div id="post-9181-score" class="comment-score"></div><div class="comment-text"><p>Anders, how to tell wireshark that, for example, 8.8.8.8 is "foo" and 4.2.2.2 is "bar" (manually resolve), when starting a new capture?</p></div><div id="comment-9181-info" class="comment-info"><span class="comment-age">(23 Feb '12, 01:37)</span> <span class="comment-user userinfo">contradictor_</span></div></div><span id="9187"></span><div id="comment-9187" class="comment"><div id="post-9187-score" class="comment-score"></div><div class="comment-text"><p>That's a separate question - see (this question)[http://ask.wireshark.org/questions/3832/how-can-i-manually-resolve-ip-addresses], and the other answer to your question, for the only current answer.</p><p>At some point it might be useful to have a UI from within Wireshark to manually add name resolution values, but no such UI currently exists.</p></div><div id="comment-9187-info" class="comment-info"><span class="comment-age">(23 Feb '12, 21:10)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="9191"></span><div id="comment-9191" class="comment"><div id="post-9191-score" class="comment-score"></div><div class="comment-text"><p>Actually if you right-click on an IP address (or, it seems a frame) in the packet-list pane then there is a "Manually resolve address" option where you can enter a IP&lt;-&gt;hostname translation. It does NOT appear to work if you right click in the packet-details pane (e.g., on an IP address).</p></div><div id="comment-9191-info" class="comment-info"><span class="comment-age">(24 Feb '12, 06:35)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-9175" class="comment-tools"></div><div class="clear"></div><div id="comment-9175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

