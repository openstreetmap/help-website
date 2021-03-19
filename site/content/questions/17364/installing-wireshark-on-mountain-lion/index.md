+++
type = "question"
title = "Installing Wireshark on Mountain LIon"
description = '''i&#x27;m installing wireshark 1.8.4 64 bit on OSX 10.8.2 macbook pro 2.7 GHz Intel Core i7. Installed XQuartz - installed the wireshark and after clicking through on the install the program is nowhere to be found. Its like it never installed - cannot locate it applications or in the directory in terminal...'''
date = "2012-12-31T16:03:00Z"
lastmod = "2013-01-31T08:06:00Z"
weight = 17364
keywords = [ "mountain", "lion", "10.8.2", "osx" ]
aliases = [ "/questions/17364" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Installing Wireshark on Mountain LIon](/questions/17364/installing-wireshark-on-mountain-lion)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17364-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i'm installing wireshark 1.8.4 64 bit on OSX 10.8.2 macbook pro 2.7 GHz Intel Core i7. Installed XQuartz - installed the wireshark and after clicking through on the install the program is nowhere to be found. Its like it never installed - cannot locate it applications or in the directory in terminal.</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags">mountain lion 10.8.2 osx</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '12, 16:03</strong></p><img src="https://secure.gravatar.com/avatar/31318b218fbc653ee0633028382a2aed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fullondan&#39;s gravatar image" /><p>fullondan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fullondan has no accepted answers">0%</span></p></div></div><div id="comments-container-17364" class="comments-container"><span id="17401"></span><div id="comment-17401" class="comment"><div id="post-17401-score" class="comment-score"></div><div class="comment-text"><p>I don't think I ever tried installing 1.8.x on my Mountain Lion machines, because I want <a href="http://ask.wireshark.org/questions/12452/where-are-the-capture-filter-options-in-wireshark-180?page=1#14019">a feature</a> that won't be in release versions until 1.10.x. So, my recommendation is to try one of the 1.9.x snapshots. If that works, then you have a feature you want that exists only in prerelease versions, too. :)</p></div><div id="comment-17401-info" class="comment-info"><span class="comment-age">(02 Jan '13, 15:02)</span> Warren Young</div></div><span id="17418"></span><div id="comment-17418" class="comment"><div id="post-17418-score" class="comment-score"></div><div class="comment-text"><p>There's no <code>Wireshark.app</code> directory in <code>/Applications</code>?</p></div><div id="comment-17418-info" class="comment-info"><span class="comment-age">(03 Jan '13, 12:03)</span> Guy Harris ♦♦</div></div><span id="17471"></span><div id="comment-17471" class="comment"><div id="post-17471-score" class="comment-score"></div><div class="comment-text"><p>The correct command to use to determine whether there's a <code>Wireshark.app</code> directory in <code>/Applications</code> is</p><pre><code>ls -ld /Applications/Wireshark.app</code></pre></div><div id="comment-17471-info" class="comment-info"><span class="comment-age">(04 Jan '13, 15:28)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-17364" class="comment-tools"></div><div class="clear"></div><div id="comment-17364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17685"></span>

<div id="answer-container-17685" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17685-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It gets installed under applications/utilities.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '13, 23:36</strong></p><img src="https://secure.gravatar.com/avatar/d32dc7b83ced776e44b0fa2916d88c21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="evanoh&#39;s gravatar image" /><p>evanoh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="evanoh has no accepted answers">0%</span></p></div></div><div id="comments-container-17685" class="comments-container"><span id="17706"></span><div id="comment-17706" class="comment"><div id="post-17706-score" class="comment-score"></div><div class="comment-text"><p>It's not <em>supposed</em> to be installed there, it's supposed to be installed in <code>/Applications</code>. Did the installer put it in <code>/Applications/Utilities</code> when you tried to install it?</p></div><div id="comment-17706-info" class="comment-info"><span class="comment-age">(15 Jan '13, 12:33)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-17685" class="comment-tools"></div><div class="clear"></div><div id="comment-17685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18184"></span>

<div id="answer-container-18184" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18184-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>the new updated in 1.8.5 version as fixed it: Macintosh:Wireshark.app $ pwd /Applications/Wireshark.app</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '13, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/31318b218fbc653ee0633028382a2aed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fullondan&#39;s gravatar image" /><p>fullondan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fullondan has no accepted answers">0%</span></p></div></div><div id="comments-container-18184" class="comments-container"></div><div id="comment-tools-18184" class="comment-tools"></div><div class="clear"></div><div id="comment-18184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

