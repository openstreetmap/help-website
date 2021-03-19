+++
type = "question"
title = "Wireshark 2 not responding when changing profiles"
description = '''Hi, I am troubleshooting why Wireshark 2.x.x stops responding when changing profiles with Windows 7 and 8.1. I don&#x27;t have any issues with 1.12.10. All the profiles were create using 1.12.x. I tried changing Virus Protection from McAffee to Norton. Any clues would be appreciated?'''
date = "2016-03-16T12:14:00Z"
lastmod = "2016-03-17T08:14:00Z"
weight = 50974
keywords = [ "profile", "hanging", "wireshark" ]
aliases = [ "/questions/50974" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 2 not responding when changing profiles](/questions/50974/wireshark-2-not-responding-when-changing-profiles)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50974-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am troubleshooting why Wireshark 2.x.x stops responding when changing profiles with Windows 7 and 8.1. I don't have any issues with 1.12.10. All the profiles were create using 1.12.x. I tried changing Virus Protection from McAffee to Norton. Any clues would be appreciated?</p></div><div id="question-tags" class="tags-container tags">profile hanging wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '16, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/a75a28c9bc7acf32bfc20ec1e984da19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dummycat&#39;s gravatar image" /><p>Dummycat<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dummycat has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Mar '16, 13:02</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-50974" class="comments-container"><span id="50976"></span><div id="comment-50976" class="comment"><div id="post-50976-score" class="comment-score"></div><div class="comment-text"><p>Do you have a capture file loaded when changing the profile? Does Wireshark ever start responding again?</p></div><div id="comment-50976-info" class="comment-info"><span class="comment-age">(16 Mar '16, 13:03)</span> grahamb ♦</div></div><span id="51533"></span><div id="comment-51533" class="comment"><div id="post-51533-score" class="comment-score"></div><div class="comment-text"><ol><li>I went back to 1.12.10 and it works.<br />
</li><li>I uninstalled 1.12.10 and installed 2.02, but didn't erase any of my configuration profiles.</li><li>Running 2.02, I try to change to a different profile. Wireshark loads the profile, but then I get the message on top "Not Responding." The only thing I can do is close Wireshark.</li><li>I deleted all my profiles and default preference and Wireshark 2.02 works without any issues.</li></ol><p>Now, I have to go line by line to figure out what 2.02 doesn't like about the profiles.</p></div><div id="comment-51533-info" class="comment-info"><span class="comment-age">(09 Apr '16, 07:32)</span> Dummycat</div></div></div><div id="comment-tools-50974" class="comment-tools"></div><div class="clear"></div><div id="comment-50974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51007"></span>

<div id="answer-container-51007" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51007-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I had a similar problem when I ran Wireshark 2.x on a Windows 7 machine. To fix the problem, I uninstalled and then re-installed Wireshark. Since after the new install, I have had no problems. Below are the details of my procedure:</p><ol><li>Perform a back-up of my current WiFi profiles (just in case)</li><li>Uninstall Wireshark 2.x, PCAP and USBCAP</li><li>Reboot PC</li><li>Re-install Wireshark 2.x, PCAP and USBCAP</li><li>Reboot PC</li></ol><p>Hope that helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '16, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span> </br></p></div></div><div id="comments-container-51007" class="comments-container"></div><div id="comment-tools-51007" class="comment-tools"></div><div class="clear"></div><div id="comment-51007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

