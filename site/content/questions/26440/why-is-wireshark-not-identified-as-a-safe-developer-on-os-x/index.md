+++
type = "question"
title = "Why is wireshark not identified as a safe developer on OS X"
description = '''When i try to install the last Wireshark 1.10.2 Intel 64.pkg on a fresh copy of Maverick OSX I get: can’t be opened because it is from an unidentified developer. I know that this can be by-passed by going to System Preferences -&amp;gt; Security &amp;amp; Privacy -&amp;gt; General -&amp;gt; Allow apps downloaded fr...'''
date = "2013-10-27T09:34:00Z"
lastmod = "2013-11-10T15:04:00Z"
weight = 26440
keywords = [ "osx", "installation", "mavericks" ]
aliases = [ "/questions/26440" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why is wireshark not identified as a safe developer on OS X](/questions/26440/why-is-wireshark-not-identified-as-a-safe-developer-on-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26440-score" class="post-score" title="current number of votes">0</div><span id="post-26440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When i try to install the last <code>Wireshark 1.10.2 Intel 64.pkg</code> on a fresh copy of Maverick OSX I get:</p><p><em>can’t be opened because it is from an unidentified developer.</em></p><p>I know that this can be by-passed by going to <em>System Preferences</em> <em>-&gt;</em> <em>Security &amp; Privacy</em> <em>-&gt;</em> <em>General</em> <em>-&gt;</em> <em>Allow apps downloaded from:</em> <em>Anywhere</em></p><p>Anyone knows the reason of it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-mavericks" rel="tag" title="see questions tagged &#39;mavericks&#39;">mavericks</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '13, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/57dca282828fcb7b6086c0a77af93ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Edmond&#39;s gravatar image" /><p><span>Edmond</span><br />
<span class="score" title="181 reputation points">181</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Edmond has 2 accepted answers">33%</span></p></div></div><div id="comments-container-26440" class="comments-container"></div><div id="comment-tools-26440" class="comment-tools"></div><div class="clear"></div><div id="comment-26440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26441"></span>

<div id="answer-container-26441" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26441-score" class="post-score" title="current number of votes">2</div><span id="post-26441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Edmond has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>We aren't signing packages yet. This should hopefully be fixed in the next few days in the development branch (1.11) and once the signatures have been tested we'll start signing the stable and legacy (1.10.x and 1.8.x) releases.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '13, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-26441" class="comments-container"><span id="26442"></span><div id="comment-26442" class="comment"><div id="post-26442-score" class="comment-score"></div><div class="comment-text"><p>Thanks Gerald for the information.</p><p>Before installing the package I spent a lot of time to find a link for the checksum (sha1sum) of the package. The only way i found them was by searching online "wireshark sha1sum 1.10.2". The second link that came up was the one which i was searching: <a href="http://www.wireshark.org/lists/wireshark-users/201309/msg00009.html">http://www.wireshark.org/lists/wireshark-users/201309/msg00009.html</a></p><p>This was not mentioned in any part of the doc's release note: <a href="http://www.wireshark.org/docs/relnotes/wireshark-1.10.2.html">http://www.wireshark.org/docs/relnotes/wireshark-1.10.2.html</a></p><p>which can be found after you go to the download wireshark page in the "Having Problem-&gt;Installation Notes" section.</p><p>This is just a hint, but it will be nice to have it :).</p><p>Thanks, Edmond.</p></div><div id="comment-26442-info" class="comment-info"><span class="comment-age">(27 Oct '13, 09:52)</span> <span class="comment-user userinfo">Edmond</span></div></div><span id="26443"></span><div id="comment-26443" class="comment"><div id="post-26443-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>I spent a lot of time to find a link for the checksum</p></blockquote><p>strange, it's directly on the download page.</p><blockquote><p><a href="http://www.wireshark.org/download.html">http://www.wireshark.org/download.html</a></p></blockquote><p>see <strong>Verify Downloads</strong></p></div><div id="comment-26443-info" class="comment-info"><span class="comment-age">(27 Oct '13, 10:36)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="26444"></span><div id="comment-26444" class="comment"><div id="post-26444-score" class="comment-score"></div><div class="comment-text"><p>You're right. I didn't see that. Thanks!</p></div><div id="comment-26444-info" class="comment-info"><span class="comment-age">(27 Oct '13, 10:40)</span> <span class="comment-user userinfo">Edmond</span></div></div><span id="26822"></span><div id="comment-26822" class="comment"><div id="post-26822-score" class="comment-score"></div><div class="comment-text"><p>As of r53243 we're now signing 64-bit development packages at <a href="http://www.wireshark.org/download/automated/osx/.">http://www.wireshark.org/download/automated/osx/.</a> I'll integrate signing for other packages over the next few days.</p></div><div id="comment-26822-info" class="comment-info"><span class="comment-age">(10 Nov '13, 14:47)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div><span id="26826"></span><div id="comment-26826" class="comment"><div id="post-26826-score" class="comment-score"></div><div class="comment-text"><p>Let us know.</p></div><div id="comment-26826-info" class="comment-info"><span class="comment-age">(10 Nov '13, 15:04)</span> <span class="comment-user userinfo">Edmond</span></div></div></div><div id="comment-tools-26441" class="comment-tools"></div><div class="clear"></div><div id="comment-26441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

