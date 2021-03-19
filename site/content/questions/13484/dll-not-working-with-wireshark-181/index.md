+++
type = "question"
title = "DLL not working with Wireshark 1.8.1"
description = '''Hi, I wrote a Wireshark Plugin on Wireshark 1.7.1 and compiled WS to generate a DLL. Now when I take this DLL and put this in Wireshark 1.8.1 I get an error saying msvcr90.dll is missing. In my Wireshark 1.8.1 installation, I checked and found that I have msvcr100.dll instead of msvcr90.dll. Please ...'''
date = "2012-08-08T23:00:00Z"
lastmod = "2012-08-09T10:16:00Z"
weight = 13484
keywords = [ "dll", "plugins" ]
aliases = [ "/questions/13484" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [DLL not working with Wireshark 1.8.1](/questions/13484/dll-not-working-with-wireshark-181)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13484-score" class="post-score" title="current number of votes">0</div><span id="post-13484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I wrote a Wireshark Plugin on Wireshark 1.7.1 and compiled WS to generate a DLL. Now when I take this DLL and put this in Wireshark 1.8.1 I get an error saying msvcr90.dll is missing. In my Wireshark 1.8.1 installation, I checked and found that I have msvcr100.dll instead of msvcr90.dll.</p><p>Please help me fix this..!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dll" rel="tag" title="see questions tagged &#39;dll&#39;">dll</span> <span class="post-tag tag-link-plugins" rel="tag" title="see questions tagged &#39;plugins&#39;">plugins</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '12, 23:00</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p><span>sid</span><br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-13484" class="comments-container"></div><div id="comment-tools-13484" class="comment-tools"></div><div class="clear"></div><div id="comment-13484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13485"></span>

<div id="answer-container-13485" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13485-score" class="post-score" title="current number of votes">1</div><span id="post-13485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark 1.8.x is built with Visual Studio 2010. You need to recompile your plugin with that version to make it work with Wireshark 1.8.x.</p><blockquote><p><code>tshark -v</code><br />
<code>TShark 1.8.0 (SVN Rev 43431 from /trunk-1.8)</code><br />
<code>Built using Microsoft Visual C++ 10.0 build 40219</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '12, 00:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Aug '12, 00:30</strong> </span></p></div></div><div id="comments-container-13485" class="comments-container"><span id="13515"></span><div id="comment-13515" class="comment"><div id="post-13515-score" class="comment-score"></div><div class="comment-text"><p>Also note that, in general, you cannot take a plugin compiled for one major.minor version (e.g., 1.7) and use it in a different major.minor version (e.g., 1.8). We do, however, <em>try</em> to maintain binary compatibility within a major.minor version (e.g., something compiled for 1.8.0 should work with 1.8.1).</p></div><div id="comment-13515-info" class="comment-info"><span class="comment-age">(09 Aug '12, 06:30)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="13519"></span><div id="comment-13519" class="comment"><div id="post-13519-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt &amp; Jeff.</p></div><div id="comment-13519-info" class="comment-info"><span class="comment-age">(09 Aug '12, 10:16)</span> <span class="comment-user userinfo">sid</span></div></div></div><div id="comment-tools-13485" class="comment-tools"></div><div class="clear"></div><div id="comment-13485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

