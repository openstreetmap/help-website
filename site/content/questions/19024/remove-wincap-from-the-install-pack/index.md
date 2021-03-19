+++
type = "question"
title = "Remove WinCap from the Install pack"
description = '''Hi, Is there any way to have an install package for WireShark that don&#x27;t deploy the WinCap (without the option to install WinCap?) I will not give the option to capture the traffic since I will provide the traffic packages to my team. I will not relly then to uninstall the WinCap after deploy the Wi...'''
date = "2013-03-01T04:03:00Z"
lastmod = "2013-03-01T09:18:00Z"
weight = 19024
keywords = [ "wincap", "install", "wireshark" ]
aliases = [ "/questions/19024" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Remove WinCap from the Install pack](/questions/19024/remove-wincap-from-the-install-pack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19024-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is there any way to have an install package for WireShark that don't deploy the WinCap (without the option to install WinCap?)</p><p>I will not give the option to capture the traffic since I will provide the traffic packages to my team. I will not relly then to uninstall the WinCap after deploy the WireShark.</p><p>Is that possible? To remove WinCap option from the install package?</p></div><div id="question-tags" class="tags-container tags">wincap install wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '13, 04:03</strong></p><img src="https://secure.gravatar.com/avatar/48bee93a50f9f34c231c278a91c03600?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bonacordi&#39;s gravatar image" /><p>Bonacordi<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bonacordi has no accepted answers">0%</span></p></div></div><div id="comments-container-19024" class="comments-container"></div><div id="comment-tools-19024" class="comment-tools"></div><div class="clear"></div><div id="comment-19024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19034"></span>

<div id="answer-container-19034" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19034-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>As @Jaap says, you can make your own installer. However, I don't really see the point. I see two possible install scenario's</p><ul><li><strong>The user is allowed to install software.</strong> Then there is nothing keeping the user from installing another version of wireshark with WinPcap included (or install WinPcap separately).</li><li><strong>The user is not allowed to install software.</strong> In this case you do the installing and you can skip the installation of WinPcap during the installation process (I'm no windows admin, but I guess you can even automate this around the vanilla installer).</li></ul><p>How do you see the use case for an installer without WinPcap included?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19034" class="comments-container"><span id="19036"></span><div id="comment-19036" class="comment"><div id="post-19036-score" class="comment-score"></div><div class="comment-text"><blockquote><p>How do you see the use case for an installer without WinPcap included?</p></blockquote><p>as part of an analysis system/package (together with other software) where Wireshark is only used to look at capture files and there is no need to capture traffic. If you want to roll out that package automatically, you would need a way to prevent the installation of Winpcap. But then, the OP could just use the portable version of Wireshark, extract it, remove WinPcap from the package and repackage it.</p></div><div id="comment-19036-info" class="comment-info"><span class="comment-age">(01 Mar '13, 09:25)</span> Kurt Knochner ♦</div></div><span id="19039"></span><div id="comment-19039" class="comment"><div id="post-19039-score" class="comment-score">1</div><div class="comment-text"><p>Oh, I do understand the use-case for not having WinPcap installed, but I think the current installer has hooks to not install WinPcap in an automated environment:</p><p>From packaging/nsis/wireshark.nsi:</p><pre><code>; if running as a silent installer, don&#39;t try to install winpcap
IfSilent SecRequired_skip_Winpcap</code></pre><p>And from <a href="http://nsis.sourceforge.net/Docs/Chapter4.html#4.12:">http://nsis.sourceforge.net/Docs/Chapter4.html#4.12:</a></p><pre><code>There are several methods to make an installer or an uninstaller silent:</code></pre><p>There are several methods to make an installer or an uninstaller silent:</p><pre><code>    SilentInstall and SilentUninstall
    SetSilent
    Passing /S on the command line (case sensitive)</code></pre><p>So starting the installer with /S should do the trick :-)</p></div><div id="comment-19039-info" class="comment-info"><span class="comment-age">(01 Mar '13, 09:38)</span> SYN-bit ♦♦</div></div><span id="19040"></span><div id="comment-19040" class="comment"><div id="post-19040-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So starting the installer with /S should do the trick :-)</p></blockquote><p>there you have it. Problem solved! :-)</p></div><div id="comment-19040-info" class="comment-info"><span class="comment-age">(01 Mar '13, 09:51)</span> Kurt Knochner ♦</div></div><span id="19043"></span><div id="comment-19043" class="comment"><div id="post-19043-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guys... It was exaclty what I was looking for.</p></div><div id="comment-19043-info" class="comment-info"><span class="comment-age">(01 Mar '13, 10:04)</span> Bonacordi</div></div><span id="19045"></span><div id="comment-19045" class="comment"><div id="post-19045-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", that's the way this site works best, please see the FAQ)</p></div><div id="comment-19045-info" class="comment-info"><span class="comment-age">(01 Mar '13, 10:10)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-19034" class="comment-tools"></div><div class="clear"></div><div id="comment-19034-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19028"></span>

<div id="answer-container-19028" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19028-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In order to do so you'll have to roll your own installer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19028" class="comments-container"><span id="19032"></span><div id="comment-19032" class="comment"><div id="post-19032-score" class="comment-score"></div><div class="comment-text"><p>Any hint or tutorial about how to do that?</p></div><div id="comment-19032-info" class="comment-info"><span class="comment-age">(01 Mar '13, 08:00)</span> Bonacordi</div></div></div><div id="comment-tools-19028" class="comment-tools"></div><div class="clear"></div><div id="comment-19028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

