+++
type = "question"
title = "QT no such slot"
description = '''Hi everyone, I&#x27;m trying to modify the sources codes of wireshark QT but apparently I can&#x27;t add new slots. I mean i added in main_windows.h my declaration,  void PingCouter(); in mainwindows_slot.cpp my code  void MainWindow::PingCounter() {   plugin_test *test = new plugin_test(this);  test-&amp;gt;show...'''
date = "2015-09-29T06:43:00Z"
lastmod = "2015-09-29T09:22:00Z"
weight = 46252
keywords = [ "qt", "wireshark" ]
aliases = [ "/questions/46252" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [QT no such slot](/questions/46252/qt-no-such-slot)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46252-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I'm trying to modify the sources codes of wireshark QT but apparently I can't add new slots. I mean i added in main_windows.h my declaration,</p><p>void PingCouter();</p><p>in mainwindows_slot.cpp my code</p><pre><code>void MainWindow::PingCounter()
{

  plugin_test *test = new plugin_test(this);
  test-&gt;show();
}</code></pre><p>and in main_windows.cpp my connect slot</p><pre><code>  QAction *Ping_Counter = new QAction;
  connect(Ping_Counter, SIGNAL(triggered()), this, SLOT(PingCounter()));</code></pre><p>I have no compilation errors but i have a runtime message :</p><pre><code>  QObject::connect: No such slot MainWindow::PingCounter()
  QObject::connect:  (receiver name: &#39;MainWindow&#39;)</code></pre><p>I watched in mocmainwindows.cpp to be sure that my slot was here but it is not. therefore i think there is a problem here but i don't know how to resolve this one.</p><p>thanks for your help</p></div><div id="question-tags" class="tags-container tags">qt wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '15, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/5bbfe79da86421b772518d0d96dbb08c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hystreal&#39;s gravatar image" /><p>Hystreal<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hystreal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Sep '15, 06:49</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-46252" class="comments-container"></div><div id="comment-tools-46252" class="comment-tools"></div><div class="clear"></div><div id="comment-46252-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46253"></span>

<div id="answer-container-46253" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46253-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should hop over to the <a href="https://www.wireshark.org/mailman/listinfo/wireshark-dev">developers mailing list</a>, that's were we all hang out discussing these things. Come and join us.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '15, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-46253" class="comments-container"><span id="46337"></span><div id="comment-46337" class="comment"><div id="post-46337-score" class="comment-score"></div><div class="comment-text"><p>Any idea ?</p><p>i sent a mail to the developers mailing list but i have no feedback.</p></div><div id="comment-46337-info" class="comment-info"><span class="comment-age">(02 Oct '15, 02:42)</span> Hystreal</div></div><span id="46599"></span><div id="comment-46599" class="comment"><div id="post-46599-score" class="comment-score"></div><div class="comment-text"><p>There was a response on the 30th, by Graham Bloice.</p></div><div id="comment-46599-info" class="comment-info"><span class="comment-age">(16 Oct '15, 00:53)</span> Jaap ♦</div></div><span id="46600"></span><div id="comment-46600" class="comment"><div id="post-46600-score" class="comment-score"></div><div class="comment-text"><p>oh sorry i'm new on this, i thought that i'll receive an email. But now i don't know how to answer.</p></div><div id="comment-46600-info" class="comment-info"><span class="comment-age">(16 Oct '15, 01:17)</span> Hystreal</div></div><span id="46607"></span><div id="comment-46607" class="comment"><div id="post-46607-score" class="comment-score"></div><div class="comment-text"><p>Have you actually used "Subscribing to Wireshark-dev"? or just dropped a mail to [email protected] ? In the former case you get echoed all discussion, in the later it's a one way street.</p><p>Anyways, you can always dig into the <a href="https://www.wireshark.org/lists/wireshark-dev/201509/msg00133.html">archive</a></p></div><div id="comment-46607-info" class="comment-info"><span class="comment-age">(16 Oct '15, 04:31)</span> Jaap ♦</div></div><span id="46685"></span><div id="comment-46685" class="comment"><div id="post-46685-score" class="comment-score"></div><div class="comment-text"><p>Yes i used "subscribing to wireshark-dev", i found my post but i don't know how to answer. i mean i don't know if i have to send another mail or if there is an answer button?</p></div><div id="comment-46685-info" class="comment-info"><span class="comment-age">(19 Oct '15, 01:07)</span> Hystreal</div></div></div><div id="comment-tools-46253" class="comment-tools"></div><div class="clear"></div><div id="comment-46253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46260"></span>

<div id="answer-container-46260" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46260-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is "void PingCouter();" listed under a "slots:" section in main_window.h? The primary difference between slots and regular C++ member functions is that the "moc" utility adds slots to a function table. Without a defined slot, "connect" won't find an entry in the table.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '15, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-46260" class="comments-container"><span id="46261"></span><div id="comment-46261" class="comment"><div id="post-46261-score" class="comment-score"></div><div class="comment-text"><p>Yes it is in public slot section</p></div><div id="comment-46261-info" class="comment-info"><span class="comment-age">(29 Sep '15, 09:24)</span> Hystreal</div></div></div><div id="comment-tools-46260" class="comment-tools"></div><div class="clear"></div><div id="comment-46260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

