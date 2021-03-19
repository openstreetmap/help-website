+++
type = "question"
title = "What is ChmodBPF folder in startup items - MacBook Pro running Mavericks"
description = '''I am having a console error appear every 5 seconds. The error is:  12/5/13 8:12:13.233 AM Wireless Network Utility[415]: Model -ioClassRef error  Apple has no idea what this error is but in the course of investigating things I discovered the directory in my startupitems directory  ChmodBPF  That dir...'''
date = "2013-12-05T05:33:00Z"
lastmod = "2013-12-06T02:29:00Z"
weight = 27806
keywords = [ "chmodbpf" ]
aliases = [ "/questions/27806" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What is ChmodBPF folder in startup items - MacBook Pro running Mavericks](/questions/27806/what-is-chmodbpf-folder-in-startup-items-macbook-pro-running-mavericks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27806-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am having a console error appear every 5 seconds. The error is:</p><blockquote><p>12/5/13 8:12:13.233 AM Wireless Network Utility[415]: Model -ioClassRef error</p></blockquote><p>Apple has no idea what this error is but in the course of investigating things I discovered the directory in my startupitems directory</p><blockquote><p>ChmodBPF</p></blockquote><p>That directory contains two items</p><blockquote><p>ChmodBPF StartupParameters.plist</p></blockquote><p>StartupParameter.plist contains</p><blockquote><p>{ Description = iNetGet; Provides = ( iNetGet, ); Requires = ( Resolver, ); }</p></blockquote><p>Apple forums have indicated that this is a remnant of Wireshark installation. I don't recall installing Wireshark but I may have and just forgotten. I'm old. In any case I'd like to remove this whether it it is part of Wireshark or not and ensure that if I did have Wireshark installed at some point in time, that it is completely uninstalled.</p><p>I do not see a Wireshark directory anywhere so I"m not sure what is going on,</p><p>Any help would be appreciated.</p></div><div id="question-tags" class="tags-container tags">chmodbpf</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '13, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/1bef277d6c83ac3030ee0ab6cdc8f7a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cnymike&#39;s gravatar image" /><p>cnymike<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cnymike has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Dec '13, 05:46</p></div></div><div id="comments-container-27806" class="comments-container"></div><div id="comment-tools-27806" class="comment-tools"></div><div class="clear"></div><div id="comment-27806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27833"></span>

<div id="answer-container-27833" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27833-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>ChmodBPF originally comes from the <a href="http://www.tcpdump.org/">libpcap</a> project. It's intended to set permissions when the system starts up in order to allow regular users to capture network packets. Wireshark's OS X installer ships with ChmodBPF but we're not necessarily the only application that does so.</p><p>In your case it looks like ChmodBPF might have been installed by <a href="http://www.etinysoft.com/inetget.html">iNetGet</a>. I'm not familiar with this application but the <em>very first</em> word of the <em>very first</em> feature is "Auto-sniff", which suggests to me that it captures packets. If you don't have Wireshark, iNetGet, or any other traffic capture application installed it's probably safe to remove ChmodBPF.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '13, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-27833" class="comments-container"><span id="27836"></span><div id="comment-27836" class="comment"><div id="post-27836-score" class="comment-score"></div><div class="comment-text"><p>Thanks Gerald for your reply.</p><p>When I purchased my new MacBook Pro, I transferred everything from my old laptop to it. I have a foggy recollection of experimenting with a packet sniffer application at one point in time, Perhaps this was a remnant of that. I'm not sure and too forgetful to remember.</p><p>I have removed it however and so far everything seems normal.</p><p>Except I am having another probably unrelated issue which is in the console I see repetitive errors every 5 seconds for:</p><p>12/5/13 1:28:41.392 PM Wireless Network Utility[415]: Model -ioClassRef error</p><p>I haven't got the faintest clue what that's all about. I do know that I have 2 MacBook Pros and one of the does not have the applicatiion this error is referencing, namely "Wireless Network Utility". My other MBP, the one generating that error, does have that application. So that application may have been brought over from my file transfer, or maybe was a remnant of Mountain Lion since I am now running Mavericks.</p><p>Very frustrating.</p></div><div id="comment-27836-info" class="comment-info"><span class="comment-age">(05 Dec '13, 10:32)</span> cnymike</div></div><span id="27859"></span><div id="comment-27859" class="comment"><div id="post-27859-score" class="comment-score"></div><div class="comment-text"><p>Yes it did. What I do not understand is that I wasn't actually running that application. Yet somehow it was a process. There must have been a startup item or something for it. In any case, deleting the application did indeed stop the error, Seems pretty obvious in retrospect but since I never actually launched the application I just figured there was some other cause.</p></div><div id="comment-27859-info" class="comment-info"><span class="comment-age">(06 Dec '13, 04:47)</span> cnymike</div></div><span id="27861"></span><div id="comment-27861" class="comment"><div id="post-27861-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-27861-info" class="comment-info"><span class="comment-age">(06 Dec '13, 04:51)</span> grahamb ♦</div></div></div><div id="comment-tools-27833" class="comment-tools"></div><div class="clear"></div><div id="comment-27833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27853"></span>

<div id="answer-container-27853" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27853-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://discussions.apple.com/message/24021513#24021513">As I suspect you discovered</a>, getting rid of the "Wireless Network Utility" app makes the errors go away.</p><p><a href="https://www.google.com/search?client=safari&amp;rls=en&amp;q=%22Wireless+Network+Utility%22+mac&amp;ie=UTF-8&amp;oe=UTF-8">Teh Google suggests</a> that it might be a utility for third-party USB Wi-Fi adapters either from Realtek or using Realtek's chips. Do you, or did you, have any USB-stick Wi-Fi adapters that you used on either your old laptop or the one onto which you transferred stuff from the old laptop?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '13, 02:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-27853" class="comments-container"></div><div id="comment-tools-27853" class="comment-tools"></div><div class="clear"></div><div id="comment-27853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

