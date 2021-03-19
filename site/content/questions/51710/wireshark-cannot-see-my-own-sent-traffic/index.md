+++
type = "question"
title = "Wireshark - cannot see my own sent traffic"
description = '''Hi folks, I have a weird issue I have been battling with for a couple of days now. I&#x27;m using a Dell Latitude E5440 on Windows 10, and up until a couple of days ago I could use Wireshark fine. It still runs and monitors traffic great on the mirror port on my switch - but all of a sudden I&#x27;m not seein...'''
date = "2016-04-15T20:22:00Z"
lastmod = "2016-04-19T19:54:00Z"
weight = 51710
keywords = [ "wireshark" ]
aliases = [ "/questions/51710" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark - cannot see my own sent traffic](/questions/51710/wireshark-cannot-see-my-own-sent-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51710-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks,</p><p>I have a weird issue I have been battling with for a couple of days now.</p><p>I'm using a Dell Latitude E5440 on Windows 10, and up until a couple of days ago I could use Wireshark fine. It still runs and monitors traffic great on the mirror port on my switch - but all of a sudden I'm not seeing my own PCs outgoing traffic.</p><p>It actually works fine, i.e. I can browse websites, use a SIP client, ping my gateway and all of that works - it just doesn't show my PCs outgoing traffic on WS. Since the problem happened I have uninstalled/reinstalled WS and WinPcap, also disabled symantec antivirus/firewall - no different. Also reinstalled network card driver.</p><p>I'm pretty sure I have removed all capture and display filters, and I doubt they would remain after reinstall (included removing personal settings).</p><p>Any ideas? One clue may be that ALL interfaces e.g. both my wired ethernet and wireless interfaces show the same symptoms?</p><p>Any ideas?</p><p>Thanks</p><p>Neil</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '16, 20:22</strong></p><img src="https://secure.gravatar.com/avatar/3fff2d1ea1b66fc5fb1d776a921a014f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Neil&#39;s gravatar image" /><p>Neil<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Neil has no accepted answers">0%</span></p></div></div><div id="comments-container-51710" class="comments-container"><span id="51712"></span><div id="comment-51712" class="comment"><div id="post-51712-score" class="comment-score"></div><div class="comment-text"><p>Comment - tried this with both WS 1.12.7 and 2.0.2, same problem.</p></div><div id="comment-51712-info" class="comment-info"><span class="comment-age">(15 Apr '16, 20:51)</span> Neil</div></div></div><div id="comment-tools-51710" class="comment-tools"></div><div class="clear"></div><div id="comment-51710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51793"></span>

<div id="answer-container-51793" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51793-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>also disabled symantec antivirus/firewall -</p></blockquote><p>sounds like the 'standard' problem we have seen a lot here. Some security software on the device might interfere with WinPcap. Please <strong>uninstall</strong> any security software, as it has been reported, that <strong>only disabling does not help</strong> in certain cases, especially with Symantec Endpoint Security, but also others.</p><p>See also my answer to a similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/28909/no-outgoing-packets">https://ask.wireshark.org/questions/28909/no-outgoing-packets</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '16, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-51793" class="comments-container"></div><div id="comment-tools-51793" class="comment-tools"></div><div class="clear"></div><div id="comment-51793-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51807"></span>

<div id="answer-container-51807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51807-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try Npcap:</p><p><a href="https://github.com/nmap/npcap/">https://github.com/nmap/npcap/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '16, 19:54</strong></p><img src="https://secure.gravatar.com/avatar/0f8ec58f46e4af3a67f768675c20aac8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yang%20Luo&#39;s gravatar image" /><p>Yang Luo<br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yang Luo has one accepted answer">4%</span></p></div></div><div id="comments-container-51807" class="comments-container"></div><div id="comment-tools-51807" class="comment-tools"></div><div class="clear"></div><div id="comment-51807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

