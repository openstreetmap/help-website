+++
type = "question"
title = "hoping to log teredo activity"
description = '''Teredo has been loaded on my computer by someone in my house. It is not currently set to on I don&#x27;t think. But I wanted to know is it possible to set up wireshark to record traffic on tereno if it is turned on at a later date so I can catch what is going on. Obviously the other user wouldn&#x27;t turn on...'''
date = "2014-06-04T14:56:00Z"
lastmod = "2014-06-04T15:25:00Z"
weight = 33409
keywords = [ "filter", "capture", "ipv6", "teredo", "router" ]
aliases = [ "/questions/33409" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [hoping to log teredo activity](/questions/33409/hoping-to-log-teredo-activity)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33409-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Teredo has been loaded on my computer by someone in my house. It is not currently set to on I don't think. But I wanted to know is it possible to set up wireshark to record traffic on tereno if it is turned on at a later date so I can catch what is going on. Obviously the other user wouldn't turn on wireshark can it be left to record while closed? Trying to understand and do this any help would be hugely appreciated.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">filter capture ipv6 teredo router</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '14, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/eb728a6714b3cfa7024766918f261f4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="crazygirl&#39;s gravatar image" /><p>crazygirl<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="crazygirl has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jun '14, 15:25</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-33409" class="comments-container"></div><div id="comment-tools-33409" class="comment-tools"></div><div class="clear"></div><div id="comment-33409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33411"></span>

<div id="answer-container-33411" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33411-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Teredo comes with Windows as a IPv6 network sub system since Windows Vista, so I doubt someone loaded it into your computer. You can verify its state by entering the following command at the command prompt:</p><pre><code>netsh interface teredo show state</code></pre><p>By default, it should show the type as "Client". For me, the command returns this:</p><pre><code>Teredo Parameters

Type                    : disabled
Server Name             : teredo.ipv6.microsoft.com.
Client Refresh Interval : 30 seconds
Client Port             : unspecified
State                   : offline
Error                   : none</code></pre><p>It's disabled for me since I turn it off on all my Windows PCs (together with ISATAP and 6to4, two other IPv6 transition techniques). You need to have an elevated ("run as administrator") command line for this:</p><pre><code>netsh interface teredo set state disabled</code></pre><p>Teredo is already pretty much obsolete by now and rarely ever used to achieve IPv6 connectivity: <a href="https://www.google.com/intl/en/ipv6/statistics.html">Google IPv6 Adoption Graph</a></p><p>If you want to track if you are sending teredo packets you can capture with Wireshark. Filter on "udp.port==3544" to see if there is traffic on that port containing "Teredo IPv6 over UDP tunneling" headers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '14, 15:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33411" class="comments-container"><span id="33448"></span><div id="comment-33448" class="comment"><div id="post-33448-score" class="comment-score"></div><div class="comment-text"><p>when I command prompt ipconfig I get my regular connection info I expected but then I also get this</p><p>Tunnel adapter isatap.Speed: dns suffix: speed local link ipv6 address: with numbers</p><p>Tunnel adapter Teredo Tunneling PSEUDO-interface IPV6 has numbers Link local IPV6 address : has letters and numbers</p><p>none of this was on until yesterday. so my question is will shark run when closed? can I set it up while closed to capture and report to me what traffic is used on teredo tunneling? how do I do that? I think my teenage son is looking at porn. any help would be hugely appreciated he is only 12.</p></div><div id="comment-33448-info" class="comment-info"><span class="comment-age">(05 Jun '14, 07:49)</span> crazygirl</div></div><span id="33450"></span><div id="comment-33450" class="comment"><div id="post-33450-score" class="comment-score"></div><div class="comment-text"><p>when I check its status it shows as client port: unspecified and its State as Dormant. how is it turned to active and sometimes dormant?</p></div><div id="comment-33450-info" class="comment-info"><span class="comment-age">(05 Jun '14, 07:52)</span> crazygirl</div></div><span id="33453"></span><div id="comment-33453" class="comment"><div id="post-33453-score" class="comment-score"></div><div class="comment-text"><p>Sure, ISATAP and Teredo interfaces exist by default unless disabled. Wireshark doesn't care about those interfaces because they are virtual interfaces that use your normal network card to communicate, so if you capture on your physical network card you can see what they are doing, too. That includes the tunneled traffic, yes.</p><p>Teredo becomes active automatically (unless completely disabled as I've shown in my answer above) when an IPv6 address is contacted and there is no IPv6 router available. So it is quite normal that in current networks it becomes active sometimes and "goes back to sleep" after a while.</p><p>Regarding the porn thing - there may be a browser history that you can check, which is less complicated than trying to understand network packets. That only works if he's not using inkognito mode though.</p></div><div id="comment-33453-info" class="comment-info"><span class="comment-age">(05 Jun '14, 07:59)</span> Jasper ♦♦</div></div></div><div id="comment-tools-33411" class="comment-tools"></div><div class="clear"></div><div id="comment-33411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

