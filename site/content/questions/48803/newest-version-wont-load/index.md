+++
type = "question"
title = "Newest version won&#x27;t load"
description = '''Just upgraded to the latest version, 2.0.1 according to the Properties of the .exe file, the one with the &quot;legacy&quot;version attached and the new USPcap addition. Well, for the first time since I started using Wireshark YEARS ago, neither version will load. The non-Legacy version starts with a window, ...'''
date = "2016-01-02T15:16:00Z"
lastmod = "2016-01-03T14:37:00Z"
weight = 48803
keywords = [ "will", "not", "load" ]
aliases = [ "/questions/48803" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Newest version won't load](/questions/48803/newest-version-wont-load)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48803-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Just upgraded to the latest version, 2.0.1 according to the Properties of the .exe file, the one with the "legacy"version attached and the new USPcap addition. Well, for the first time since I started using Wireshark YEARS ago, neither version will load. The non-Legacy version starts with a window, shows the components being loaded up to what seems to be the last piece, then becomes "Not responding", and I must kill the process. Then I tried the legacy version, which seems to start as the the older versions did with a small window showing the components loading, again seems to get to the last piece then also becomes "not responding" and must be killed. Is this the first version by this Riverbed company? I used the "check for upgrade" from within the last version, even though it was Secunia PSI that tipped me off an upgrade was available.</p><p>Any ideas folks?</p></div><div id="question-tags" class="tags-container tags">will not load</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '16, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/8ddef190e1b62ba203b35d03dabbbef7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="survivor7812&#39;s gravatar image" /><p>survivor7812<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="survivor7812 has no accepted answers">0%</span></p></div></div><div id="comments-container-48803" class="comments-container"></div><div id="comment-tools-48803" class="comment-tools"></div><div class="clear"></div><div id="comment-48803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="48804"></span>

<div id="answer-container-48804" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48804-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do you have a configuration directory (<a href="https://www.wireshark.org/docs/wsug_html_chunked/ChAppFilesConfigurationSection.html">%APPDATA%\Wireshark</a>) left over from the last time you used Wireshark? If so, can you try renaming it?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '16, 15:27</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jan '16, 15:29</p></div></div><div id="comments-container-48804" class="comments-container"></div><div id="comment-tools-48804" class="comment-tools"></div><div class="clear"></div><div id="comment-48804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48807"></span>

<div id="answer-container-48807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48807-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is generally a symptom of an issue in WinPcap, the mechanism used to capture traffic on Windows. Wireshark uses WinPcap at startup to query the list of interfaces that can be used for captures.</p><p>The actual issue has never been resolved, but uninstalling Wireshark, uninstalling WinPcap, if it remains, ensuring that there is no copy of npf.sys in %WINDIR%\system32\drivers\, reboot, and then reinstalling Wireshark (installing WinPcap when offered) usually does the trick. Make sure you run the installer as Administrator, it should do this automatically, but if you don't get asked for permissions, cancel, then right-click the installer and select "Run as Administrator".</p><p>Riverbed has been sponsoring Wireshark for some time, but Wireshark is still produced and maintained by volunteers led by @Gerald Combs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '16, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Apr '16, 03:22</p></div></div><div id="comments-container-48807" class="comments-container"></div><div id="comment-tools-48807" class="comment-tools"></div><div class="clear"></div><div id="comment-48807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48812"></span>

<div id="answer-container-48812" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48812-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks, folks, but the problem self resolved after a reboot or three, as tech problems are wont to do. I have now gotten both the legacy and non-legacy versions to work.</p><p>Thanks, again! Good to see the program is still maintained by the author, so I hope Riverbed pays him well! :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '16, 14:37</strong></p><img src="https://secure.gravatar.com/avatar/8ddef190e1b62ba203b35d03dabbbef7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="survivor7812&#39;s gravatar image" /><p>survivor7812<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="survivor7812 has no accepted answers">0%</span></p></div></div><div id="comments-container-48812" class="comments-container"><span id="51862"></span><div id="comment-51862" class="comment"><div id="post-51862-score" class="comment-score"></div><div class="comment-text"><p>Same for me ...</p></div><div id="comment-51862-info" class="comment-info"><span class="comment-age">(22 Apr '16, 01:00)</span> robert_</div></div></div><div id="comment-tools-48812" class="comment-tools"></div><div class="clear"></div><div id="comment-48812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

