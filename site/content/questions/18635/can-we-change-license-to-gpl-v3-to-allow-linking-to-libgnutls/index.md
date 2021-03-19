+++
type = "question"
title = "Can we change license to GPL v3 to allow linking to libgnutls?"
description = '''As the title requests, is there any reason to not change to GPLv3? As Gerald has commented on in the past (found on this site thanks to Google), and as discussed in various other places ( https://bugzilla.novell.com/show_bug.cgi?id=775737 ) the license for dependencies used for decrypting SSL traffi...'''
date = "2013-02-14T09:00:00Z"
lastmod = "2013-02-14T09:52:00Z"
weight = 18635
keywords = [ "gpl", "license" ]
aliases = [ "/questions/18635" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can we change license to GPL v3 to allow linking to libgnutls?](/questions/18635/can-we-change-license-to-gpl-v3-to-allow-linking-to-libgnutls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18635-score" class="post-score" title="current number of votes">0</div><span id="post-18635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As the title requests, is there any reason to not change to GPLv3? As Gerald has commented on in the past (found on this site thanks to Google), and as discussed in various other places ( <a href="https://bugzilla.novell.com/show_bug.cgi?id=775737">https://bugzilla.novell.com/show_bug.cgi?id=775737</a> ) the license for dependencies used for decrypting SSL traffic has moved to GPLv3 and as a result it is no longer permissible to link to those libraries from something using GPLv2, or something (I am not a lawyer). Are there any reasons to stick with GPLv2 at this point? My understanding of the newer license is that it is a bit more forceful in its rules around really, truly being free, but there are countless articles online talking about that and the FSF has some helpful guides worth reviewing for those interested.</p><p><a href="http://www.gnu.org/licenses/gpl-faq.html#AllCompatibility">http://www.gnu.org/licenses/gpl-faq.html#AllCompatibility</a></p><p><a href="http://www.wireshark.org/lists/wireshark-dev/201205/msg00167.html">http://www.wireshark.org/lists/wireshark-dev/201205/msg00167.html</a></p><p><a href="https://wireshark.org/lists/wireshark-dev/201203/msg00171.html">https://wireshark.org/lists/wireshark-dev/201203/msg00171.html</a></p><p>Thanks, AB</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gpl" rel="tag" title="see questions tagged &#39;gpl&#39;">gpl</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '13, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/5e3d0d9274e8f74936c85b39491c8c57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dajoker&#39;s gravatar image" /><p><span>dajoker</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dajoker has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Feb '13, 09:42</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-18635" class="comments-container"></div><div id="comment-tools-18635" class="comment-tools"></div><div class="clear"></div><div id="comment-18635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18637"></span>

<div id="answer-container-18637" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18637-score" class="post-score" title="current number of votes">0</div><span id="post-18637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>GnuTLS is LGPLv3+ due to a dependency on GMP. There have been discussions about <a href="http://gmplib.org/list-archives/gmp-devel/2012-May/002356.html">dual-licensing GMP as LGPLv3+ / GPLv2+ in the past</a> but as far as I know no action has been taken. I don't know how the other Wireshark developers feel, but I think that:</p><ul><li>Being forced to change our license by a library that we don't directly use is a bunch of crap. I'd prefer that the Wireshark developer community direct our licensing decisions, not GMP.</li><li>If we're going to change the license so we can link with GnuTLS, why not change it so that we can link with other SSL libraries (the obvious one being OpenSSL)?</li></ul><hr /><p><strong>Update</strong>: GnuTLS switched back to LGPLv2.1+ in version 3.1.10.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '13, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Apr '13, 12:22</strong> </span></p></div></div><div id="comments-container-18637" class="comments-container"><span id="18638"></span><div id="comment-18638" class="comment"><div id="post-18638-score" class="comment-score"></div><div class="comment-text"><p>Gerald,</p><p>Thank-you for the quick response. I agree, needing to change a license because of something you do not even use (GMP in this case) would be frustrating. Perhaps I should have focused more on the end goal rather than one possible solution to the problem, and perhaps your second bullet point moves toward that goal: How do we get SSL decryption working for Linux in the long run?</p><p>I do not have any particularly strong ties to GnuTLS vs. OpenSSL. The Apache license works well for me in many cases and this "Apache-style" license used by OpenSSL would be just fine by me too (not that I count).</p></div><div id="comment-18638-info" class="comment-info"><span class="comment-age">(14 Feb '13, 09:52)</span> <span class="comment-user userinfo">dajoker</span></div></div></div><div id="comment-tools-18637" class="comment-tools"></div><div class="clear"></div><div id="comment-18637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

