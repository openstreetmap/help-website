+++
type = "question"
title = "kerberos library requires -lcrypto but --with-ssl not specified"
description = '''Okay so attempting to configure this on FreeBSD 9.2, the config script checks for kb5, checks for the kb5 config file, and then I get this error:  $ Kerberos library requires -lcrypto but --with-ssl not specified $ rm: *.core: invalid argument $ rm: core.conftest.*: invalid argument  I&#x27;m sort of new...'''
date = "2014-03-08T11:36:00Z"
lastmod = "2014-03-09T03:51:00Z"
weight = 30603
keywords = [ "kerberos", "configure", "error" ]
aliases = [ "/questions/30603" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [kerberos library requires -lcrypto but --with-ssl not specified](/questions/30603/kerberos-library-requires-lcrypto-but-with-ssl-not-specified)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30603-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Okay so attempting to configure this on FreeBSD 9.2, the config script checks for kb5, checks for the kb5 config file, and then I get this error:</p><ol><li>$ Kerberos library requires -lcrypto but --with-ssl not specified</li><li>$ rm: *.core: invalid argument</li><li>$ rm: core.conftest.*: invalid argument</li></ol><p>I'm sort of new to UNIX so if someone can help me figure out how to configure Kerberos properly for this installation I'd really appreciate it. thanks, jim</p></div><div id="question-tags" class="tags-container tags">kerberos configure error</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '14, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/4f713d2d9d447724a6f15177137d0e1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="earthworm987&#39;s gravatar image" /><p>earthworm987<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="earthworm987 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '14, 15:26</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-30603" class="comments-container"><span id="30621"></span><div id="comment-30621" class="comment"><div id="post-30621-score" class="comment-score"></div><div class="comment-text"><p>Hint: If you are (totally) rewriting your original question (including the title), you are kind of 'subverting' the purpose of this site. That way, nobody will be able to understand the given answers. Please don't do that. Thank you!</p></div><div id="comment-30621-info" class="comment-info"><span class="comment-age">(09 Mar '14, 11:47)</span> Kurt Knochner ♦</div></div><span id="30623"></span><div id="comment-30623" class="comment"><div id="post-30623-score" class="comment-score"></div><div class="comment-text"><p>I've reverted to the original version of the question, and made the second question into a separate question.</p></div><div id="comment-30623-info" class="comment-info"><span class="comment-age">(09 Mar '14, 15:24)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-30603" class="comment-tools"></div><div class="clear"></div><div id="comment-30603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30613"></span>

<div id="answer-container-30613" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30613-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>$ Kerberos library requires -lcrypto but --with-ssl not specified</p></blockquote><p>sounds like the error message tells you what to do. Add <strong>--with-ssl</strong> to the <code>configure</code> options (./configure --with-ssl --whatever-other-options-you-chose).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '14, 03:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '14, 23:02</p></div></div><div id="comments-container-30613" class="comments-container"><span id="30624"></span><div id="comment-30624" class="comment"><div id="post-30624-score" class="comment-score"></div><div class="comment-text"><p>In the trunk, I've changed the message to</p><pre><code>Kerberos library requires -lcrypto, so you must specify --with-ssl</code></pre><p>in the hope that it'll make it clearer what the solution to the problem is.</p></div><div id="comment-30624-info" class="comment-info"><span class="comment-age">(09 Mar '14, 15:44)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-30613" class="comment-tools"></div><div class="clear"></div><div id="comment-30613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

