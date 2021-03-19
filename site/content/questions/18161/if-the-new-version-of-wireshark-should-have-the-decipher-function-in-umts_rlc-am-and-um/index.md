+++
type = "question"
title = "if the new version of wireshark should have the decipher function in umts_rlc AM and UM?"
description = '''if the new version of wireshark should have the decipher function in umts_rlc AM and UM? I&#x27;m desired to have new wireshark which could help me to decipher in ciphered message.'''
date = "2013-01-31T02:24:00Z"
lastmod = "2013-02-05T01:39:00Z"
weight = 18161
keywords = [ "decipher", "um", "am", "rlc" ]
aliases = [ "/questions/18161" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [if the new version of wireshark should have the decipher function in umts\_rlc AM and UM?](/questions/18161/if-the-new-version-of-wireshark-should-have-the-decipher-function-in-umts_rlc-am-and-um)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18161-score" class="post-score" title="current number of votes">0</div><span id="post-18161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>if the new version of wireshark should have the decipher function in umts_rlc AM and UM?</p><p>I'm desired to have new wireshark which could help me to decipher in ciphered message.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decipher" rel="tag" title="see questions tagged &#39;decipher&#39;">decipher</span> <span class="post-tag tag-link-um" rel="tag" title="see questions tagged &#39;um&#39;">um</span> <span class="post-tag tag-link-am" rel="tag" title="see questions tagged &#39;am&#39;">am</span> <span class="post-tag tag-link-rlc" rel="tag" title="see questions tagged &#39;rlc&#39;">rlc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '13, 02:24</strong></p><img src="https://secure.gravatar.com/avatar/f6eeed42d5aadabfed2ca2cb1faabff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smilezuzu&#39;s gravatar image" /><p><span>smilezuzu</span><br />
<span class="score" title="20 reputation points">20</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smilezuzu has no accepted answers">0%</span></p></div></div><div id="comments-container-18161" class="comments-container"></div><div id="comment-tools-18161" class="comment-tools"></div><div class="clear"></div><div id="comment-18161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18179"></span>

<div id="answer-container-18179" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18179-score" class="post-score" title="current number of votes">0</div><span id="post-18179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>deciphering code cannot be included by default due to patent restriction (see <a href="http://www.etsi.org/services/security-algorithms/3gpp-algorithms">http://www.etsi.org/services/security-algorithms/3gpp-algorithms</a> and <a href="http://www.gsma.com/technicalprojects/fraud-security/security-algorithms).">http://www.gsma.com/technicalprojects/fraud-security/security-algorithms).</a></p><p>That said in current Wireshark development version (a.k.a. 1.9 version, nightly builds can be found here: <a href="http://www.wireshark.org/download/automated/)">http://www.wireshark.org/download/automated/)</a> has a partial support of the KASUMI deciphering. But you need to add yourself the KASUMI engine source code (it's already in the 3GPP specs if I remember correctly) and recompile the source code after modifying the epan/crypt/kasumi.h file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '13, 05:06</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-18179" class="comments-container"><span id="18212"></span><div id="comment-18212" class="comment"><div id="post-18212-score" class="comment-score"></div><div class="comment-text"><p>a.k.a. 1.9 version?? wireshark1.9.? have been released?</p><p>The latest version is wireshark1.8.5 on the download website.</p></div><div id="comment-18212-info" class="comment-info"><span class="comment-age">(31 Jan '13, 19:46)</span> <span class="comment-user userinfo">smilezuzu</span></div></div><span id="18220"></span><div id="comment-18220" class="comment"><div id="post-18220-score" class="comment-score"></div><div class="comment-text"><p>"development version (a.k.a. 1.9 version,..." - means just that the verson under development that will eventually be released, possibly as 1.10. We do supply builds of the development tree for people to try out.</p></div><div id="comment-18220-info" class="comment-info"><span class="comment-age">(31 Jan '13, 22:59)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="18308"></span><div id="comment-18308" class="comment"><div id="post-18308-score" class="comment-score"></div><div class="comment-text"><p>where could I get the latest development version? Thanks!</p></div><div id="comment-18308-info" class="comment-info"><span class="comment-age">(05 Feb '13, 01:29)</span> <span class="comment-user userinfo">smilezuzu</span></div></div><span id="18309"></span><div id="comment-18309" class="comment"><div id="post-18309-score" class="comment-score"></div><div class="comment-text"><p><a href="http://www.wireshark.org/download/automated/">here</a></p></div><div id="comment-18309-info" class="comment-info"><span class="comment-age">(05 Feb '13, 01:39)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-18179" class="comment-tools"></div><div class="clear"></div><div id="comment-18179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

