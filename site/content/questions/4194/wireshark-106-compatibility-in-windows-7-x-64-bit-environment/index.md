+++
type = "question"
title = "Wireshark 1.0.6 - Compatibility in Windows 7 x 64 bit environment"
description = '''Hi, We use “Wireshark 1.0.6” in Windows Vista. I was trying to run this in Windows 7 x 64 bit environment and was getting the below error when the shortcut is launched. &quot;The NPF driver isn&#x27;t running. You may have trouble capturing or listing interfaces.&quot; Please let me know whether this is compatible...'''
date = "2011-05-24T07:34:00Z"
lastmod = "2012-02-03T07:27:00Z"
weight = 4194
keywords = [ "windows", "win64", "interfaces", "compatibility", "error" ]
aliases = [ "/questions/4194" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.0.6 - Compatibility in Windows 7 x 64 bit environment](/questions/4194/wireshark-106-compatibility-in-windows-7-x-64-bit-environment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4194-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We use “Wireshark 1.0.6” in Windows Vista. I was trying to run this in Windows 7 x 64 bit environment and was getting the below error when the shortcut is launched.</p><p>"The NPF driver isn't running. You may have trouble capturing or listing interfaces."</p><p>Please let me know whether this is compatible with Windows 7 x64 bit environment.</p></div><div id="question-tags" class="tags-container tags">windows win64 interfaces compatibility error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '11, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/702468e304e8b2cef3aa85ad5fc9ec5e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chevron&#39;s gravatar image" /><p>Chevron<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chevron has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 25 May '11, 21:39</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4194" class="comments-container"><span id="4205"></span><div id="comment-4205" class="comment"><div id="post-4205-score" class="comment-score">3</div><div class="comment-text"><p>What version of WinPcap comes with Wireshark 1.0.6? WinPcap 4.1 was the first version to support 64-bit Windows, so if an earlier version of WinPcap came with 1.0.6, you will either have to manually install a newer version of WinPcap or switch to a newer version of Wireshark.</p><p>I also don't know whether WinPcap supports, on 64-bit Windows, 32-bit applications using it. If not, you will probably have to upgrade to a newer version of WinPcap built 64-bit.</p></div><div id="comment-4205-info" class="comment-info"><span class="comment-age">(24 May '11, 15:54)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-4194" class="comment-tools"></div><div class="clear"></div><div id="comment-4194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="4208"></span>

<div id="answer-container-4208" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4208-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark 1.0.<em>x</em> shipped (note the past tense) with WinPcap 4.0.2. As Guy points out, WinPcap didn't officially support Windows 7 x64 until 4.1. You might try installing a newer release of WinPcap separately but you might run into additional problems. 64-bit Windows support was greatly improved in Wireshark 1.2 and has steadily improved since.</p><p>You should consider installing Wireshark 1.4 or the upcoming 1.6 release. As the <a href="http://wiki.wireshark.org/Development/LifeCycle">Release Life Cycle</a> page on the wiki points out, 1.0 reached end of life last year and 1.2 will reach EOL in a few weeks.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '11, 16:16</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-4208" class="comments-container"></div><div id="comment-tools-4208" class="comment-tools"></div><div class="clear"></div><div id="comment-4208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4195"></span>

<div id="answer-container-4195" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4195-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all - is there any reason why you don't move to 1.2.x or 1.4.x?</p><p>Otherwise you should check in the windows services if the NPF service is installed and started, otherwise you are not allowed to capture network data unless starting Wireshark with administrative rights.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '11, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4195" class="comments-container"><span id="4196"></span><div id="comment-4196" class="comment"><div id="post-4196-score" class="comment-score"></div><div class="comment-text"><p>We just need to make sure whether this works with Windows 7. If not we will move to higher version.</p><p>I have checked the regisrty value of "start" under HKEY_LOCAL_MACHINESYSTEMCurrentControlSetServicesNPF and it was 3. Changed it to 2.</p><p>But when I try the command "net start npf" I am getting the following error</p><p>"System error 1275 has occured. this driver has been blocked from loading"</p></div><div id="comment-4196-info" class="comment-info"><span class="comment-age">(24 May '11, 08:06)</span> Chevron</div></div><span id="4197"></span><div id="comment-4197" class="comment"><div id="post-4197-score" class="comment-score"></div><div class="comment-text"><p>Maybe it is blocked by Windows x64 because it isn't signed or not signed correctly/outdated. Windows x64 only allows signed drivers to be loaded.</p></div><div id="comment-4197-info" class="comment-info"><span class="comment-age">(24 May '11, 08:09)</span> Jasper ♦♦</div></div><span id="8829"></span><div id="comment-8829" class="comment"><div id="post-8829-score" class="comment-score"></div><div class="comment-text"><p>I suspect (as has been said in a number of places in comments) that it only allows 64-bit drivers to be loaded; the drivers in the version of WinPcap bundled with WinPcap 1.0.6 are, as per Gerald's comment, <em>NOT</em> 64-bit drivers, and will not and <em>CAN</em> not be loaded by 64-bit Windows.</p></div><div id="comment-8829-info" class="comment-info"><span class="comment-age">(04 Feb '12, 16:17)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-4195" class="comment-tools"></div><div class="clear"></div><div id="comment-4195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8806"></span>

<div id="answer-container-8806" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8806-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try running Wireshark as administrator. That worked for me.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '12, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/488b59d3b1899e76f9ce6f352e15e49c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ePlurb_admin&#39;s gravatar image" /><p>ePlurb_admin<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ePlurb_admin has no accepted answers">0%</span></p></div></div><div id="comments-container-8806" class="comments-container"><span id="8812"></span><div id="comment-8812" class="comment"><div id="post-8812-score" class="comment-score"></div><div class="comment-text"><p>Running Wireshark <em>1.0.6</em> as administrator worked on <em>64-bit Windows 7</em>? If so, then you must have installed a newer version of WinPcap, as the version of WinPcap bundled with Wireshark 1.0.6 does <em>NOT</em> support 64-bit Windows.</p></div><div id="comment-8812-info" class="comment-info"><span class="comment-age">(03 Feb '12, 10:41)</span> Guy Harris ♦♦</div></div><span id="8817"></span><div id="comment-8817" class="comment"><div id="post-8817-score" class="comment-score"></div><div class="comment-text"><p>You might also want to think very carefully about running Wireshark with Administrator privileges because of security concerns. See the <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">Capture Privileges</a> wiki page for more info.</p></div><div id="comment-8817-info" class="comment-info"><span class="comment-age">(03 Feb '12, 15:40)</span> grahamb ♦</div></div></div><div id="comment-tools-8806" class="comment-tools"></div><div class="clear"></div><div id="comment-8806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

