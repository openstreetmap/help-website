+++
type = "question"
title = "Is there an easy way to update my own plugin?"
description = '''I have previously developed a plugin. It works quite well, but now after installing the new version of Wireshark (1.8.1), it doesn&#x27;t work anymore. I think it is because it was built with version 1.7.0. Is there an easy way to get it working on 1.8.1? Do I have to download the sources again, compile ...'''
date = "2012-08-13T14:51:00Z"
lastmod = "2012-08-13T15:04:00Z"
weight = 13594
keywords = [ "development", "version", "plugin" ]
aliases = [ "/questions/13594" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there an easy way to update my own plugin?](/questions/13594/is-there-an-easy-way-to-update-my-own-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13594-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have previously developed a plugin. It works quite well, but now after installing the new version of Wireshark (1.8.1), it doesn't work anymore.</p><p>I think it is because it was built with version 1.7.0.</p><p>Is there an easy way to get it working on 1.8.1? Do I have to download the sources again, compile it, and than recompile my plugin?</p></div><div id="question-tags" class="tags-container tags">development version plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '12, 14:51</strong></p><img src="https://secure.gravatar.com/avatar/b19995667dd7e285be5ed8c1ac50cf74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anthracis&#39;s gravatar image" /><p>Anthracis<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anthracis has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Aug '12, 12:51</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-13594" class="comments-container"></div><div id="comment-tools-13594" class="comment-tools"></div><div class="clear"></div><div id="comment-13594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13597"></span>

<div id="answer-container-13597" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13597-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>We try to keep the API stable within a stable release branch (1.6.x, 1.8.x etc), but between branches there might be some code changes that break plugins compiled for other releases.</p><p>So yes, you should recompile your plugin to make it work with the 1.8 release.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '12, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-13597" class="comments-container"><span id="13771"></span><div id="comment-13771" class="comment"><div id="post-13771-score" class="comment-score"></div><div class="comment-text"><p>@SYN-bit , is there backward compatibility ? If i make plugin with VS2010 , will it work with 1.7.x releases of wireshark ?</p></div><div id="comment-13771-info" class="comment-info"><span class="comment-age">(20 Aug '12, 12:25)</span> yogeshg</div></div><span id="13775"></span><div id="comment-13775" class="comment"><div id="post-13775-score" class="comment-score"></div><div class="comment-text"><p>We make no claims of compatibility with development builds such as the 1.7.x builds.</p><p>We also make no claims of backwards compatibility with official releases - if you build for 1.8.x with VS2010, there is no guarantee that the plugin will work with 1.6.x or earlier.</p></div><div id="comment-13775-info" class="comment-info"><span class="comment-age">(20 Aug '12, 13:59)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-13597" class="comment-tools"></div><div class="clear"></div><div id="comment-13597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

