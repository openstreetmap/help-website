+++
type = "question"
title = "How to verify signature on the text file containing hashes (of Wireshark binaries)"
description = '''How to verify signature on the text file containing hashes (of Wireshark binaries) using gpg4win 2.1.0? Tried several times, says signature invalid'''
date = "2012-05-28T00:51:00Z"
lastmod = "2012-05-28T01:58:00Z"
weight = 11417
keywords = [ "gpg", "verification", "pgp", "signature" ]
aliases = [ "/questions/11417" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to verify signature on the text file containing hashes (of Wireshark binaries)](/questions/11417/how-to-verify-signature-on-the-text-file-containing-hashes-of-wireshark-binaries)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11417-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to verify signature on the text file containing hashes (of Wireshark binaries) using gpg4win 2.1.0?</p><p>Tried several times, says signature invalid</p></div><div id="question-tags" class="tags-container tags">gpg verification pgp signature</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '12, 00:51</strong></p><img src="https://secure.gravatar.com/avatar/c943a0f1bee34ffa6329d0b329ca9f2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hans&#39;s gravatar image" /><p>Hans<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hans has no accepted answers">0%</span></p></div></div><div id="comments-container-11417" class="comments-container"></div><div id="comment-tools-11417" class="comment-tools"></div><div class="clear"></div><div id="comment-11417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11420"></span>

<div id="answer-container-11420" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11420-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>this works on my system:</p><ol><li>Download the wireshark PGP Key: <a href="http://www.wireshark.org/download/gerald_at_wireshark_dot_org.gpg">http://www.wireshark.org/download/gerald_at_wireshark_dot_org.gpg</a></li><li>Download the signature file: <a href="http://www.wireshark.org/download/SIGNATURES-1.6.8.txt">http://www.wireshark.org/download/SIGNATURES-1.6.8.txt</a></li><li>Import the wireshark key into Kleopatra</li><li><strong>IMPORTANT</strong>: You'll have to sign the wireshark key with your own PGP key in Kleopatra (right-click, certify), otherwise it will not be trusted by your system.</li><li>Right-click the signature (hash) file in Windows Explorer and select "GpgEx -&gt; Verify/Check"</li><li>Unselect the first check-box (right below the file name): "Input file is a ..."</li></ol><p>Result: The signature will be shown as "valid"</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '12, 01:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 May '12, 02:34</p></div></div><div id="comments-container-11420" class="comments-container"><span id="11423"></span><div id="comment-11423" class="comment"><div id="post-11423-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>Thanks for such a to the point reply.</p><p>Was doing steps 1-5 earlier. Step 6 was the key.</p><p>cheers, Hans</p></div><div id="comment-11423-info" class="comment-info"><span class="comment-age">(28 May '12, 06:13)</span> Hans</div></div><span id="11427"></span><div id="comment-11427" class="comment"><div id="post-11427-score" class="comment-score"></div><div class="comment-text"><p>@ Hans: 1) This was a comment on Kurt's answer, please enter it as such. 2) If this was the correct answer click the checkmark so it is marked as such.</p></div><div id="comment-11427-info" class="comment-info"><span class="comment-age">(28 May '12, 06:38)</span> Jaap ♦</div></div></div><div id="comment-tools-11420" class="comment-tools"></div><div class="clear"></div><div id="comment-11420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

