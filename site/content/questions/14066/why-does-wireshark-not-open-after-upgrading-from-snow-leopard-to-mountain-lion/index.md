+++
type = "question"
title = "Why does Wireshark not open after upgrading from Snow Leopard to Mountain Lion?"
description = '''I recently installed Mountain Lion and then Wireshark stopped working. Before, with Snow Leopard, Wireshark worked well. I upgraded X11 to the latest version, but if I launch Wireshark (even with X11 already running), nothing seems to happen. Any ideas? Thanks and greeting from Italy. '''
date = "2012-09-05T16:00:00Z"
lastmod = "2012-09-05T16:39:00Z"
weight = 14066
keywords = [ "x11", "osx", "mountain-lion" ]
aliases = [ "/questions/14066" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why does Wireshark not open after upgrading from Snow Leopard to Mountain Lion?](/questions/14066/why-does-wireshark-not-open-after-upgrading-from-snow-leopard-to-mountain-lion)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14066-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently installed Mountain Lion and then Wireshark stopped working. Before, with Snow Leopard, Wireshark worked well. I upgraded X11 to the latest version, but if I launch Wireshark (even with X11 already running), nothing seems to happen. Any ideas? Thanks and greeting from Italy.</p></div><div id="question-tags" class="tags-container tags">x11 osx mountain-lion</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '12, 16:00</strong></p><img src="https://secure.gravatar.com/avatar/b753d4f23394391316454795cbcf6036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlogiga&#39;s gravatar image" /><p>carlogiga<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlogiga has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Sep '12, 16:41</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-14066" class="comments-container"><span id="14071"></span><div id="comment-14071" class="comment"><div id="post-14071-score" class="comment-score">1</div><div class="comment-text"><p>You might want to have a look at <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3760">bug 3760</a>; it <em>might</em> be relevant.</p></div><div id="comment-14071-info" class="comment-info"><span class="comment-age">(05 Sep '12, 16:48)</span> cmaynard ♦♦</div></div><span id="14073"></span><div id="comment-14073" class="comment"><div id="post-14073-score" class="comment-score"></div><div class="comment-text"><p>Possibly, but it seems like the symptom of that particular bug (which is not stated in the report) would be that Wireshark opens but displays no capture interfaces because the privilege-setting script is not run at startup (since ML doesn't support startup items). For the problem here (<em>"nothing seems to happen"</em>), it sounds like the user does not see the main Wireshark window at all.</p></div><div id="comment-14073-info" class="comment-info"><span class="comment-age">(05 Sep '12, 16:57)</span> helloworld</div></div><span id="14099"></span><div id="comment-14099" class="comment"><div id="post-14099-score" class="comment-score"></div><div class="comment-text"><p>Actually, my machine <em>does</em> continue to support startup items, including ChmodBPF, since I upgraded it from Lion to Mountain Lion.</p></div><div id="comment-14099-info" class="comment-info"><span class="comment-age">(06 Sep '12, 15:48)</span> Guy Harris ♦♦</div></div><span id="14146"></span><div id="comment-14146" class="comment"><div id="post-14146-score" class="comment-score"></div><div class="comment-text"><p>Finally resolved (!) after installing ChmodBPF (thanks cmaynard!).</p></div><div id="comment-14146-info" class="comment-info"><span class="comment-age">(09 Sep '12, 11:19)</span> carlogiga</div></div></div><div id="comment-tools-14066" class="comment-tools"></div><div class="clear"></div><div id="comment-14066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14068"></span>

<div id="answer-container-14068" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14068-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I assume you installed <a href="http://xquartz.macosforge.org/landing/">XQuartz</a> on ML. I suggest uninstalling Wireshark and reinstalling a fresh copy (by dragging the Wireshark icon from your Application directory to the Trash, and then running the Mac installer for Wireshark).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Sep '12, 16:39</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-14068" class="comments-container"></div><div id="comment-tools-14068" class="comment-tools"></div><div class="clear"></div><div id="comment-14068-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

