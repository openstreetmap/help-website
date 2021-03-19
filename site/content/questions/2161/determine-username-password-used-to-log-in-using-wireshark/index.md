+++
type = "question"
title = "Determine username &amp; password used to log in using wireshark?"
description = '''can you figure out the username and password looking at captured packet below. download file telnet-cooked.pcap (9kb) from http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;amp;do=view&amp;amp;target=telnet-cooked.pcap and open it with wireshark and determine the username and password that was ...'''
date = "2011-02-04T15:09:00Z"
lastmod = "2011-02-04T16:26:00Z"
weight = 2161
keywords = [ "username", "password", "telnet", "wireshark" ]
aliases = [ "/questions/2161" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Determine username & password used to log in using wireshark?](/questions/2161/determine-username-password-used-to-log-in-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2161-score" class="post-score" title="current number of votes">0</div><span id="post-2161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>can you figure out the username and password looking at captured packet below. download file telnet-cooked.pcap (9kb) from <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=telnet-cooked.pcap">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=telnet-cooked.pcap</a> and open it with wireshark and determine the username and password that was used to log in. also state which packet no. thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-username" rel="tag" title="see questions tagged &#39;username&#39;">username</span> <span class="post-tag tag-link-password" rel="tag" title="see questions tagged &#39;password&#39;">password</span> <span class="post-tag tag-link-telnet" rel="tag" title="see questions tagged &#39;telnet&#39;">telnet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '11, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/ede6543ddc7bdd8d826a6f712e4f5b43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="momoboyus&#39;s gravatar image" /><p><span>momoboyus</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="momoboyus has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Feb '11, 16:34</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-2161" class="comments-container"></div><div id="comment-tools-2161" class="comment-tools"></div><div class="clear"></div><div id="comment-2161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2162"></span>

<div id="answer-container-2162" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2162-score" class="post-score" title="current number of votes">2</div><span id="post-2162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Username is fake -- frame 31</p><p>Password is user -- frame 38</p><p>It is easiest just to right click an "follow tcp stream".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '11, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-2162" class="comments-container"></div><div id="comment-tools-2162" class="comment-tools"></div><div class="clear"></div><div id="comment-2162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

