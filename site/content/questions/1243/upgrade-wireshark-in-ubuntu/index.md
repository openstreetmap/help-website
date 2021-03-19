+++
type = "question"
title = "Upgrade wireshark in Ubuntu?"
description = '''Is it possible to upgrade wireshark in Ubuntu? If so, how can a linux-newby do this?'''
date = "2010-12-04T05:09:00Z"
lastmod = "2011-01-03T18:08:00Z"
weight = 1243
keywords = [ "upgrade", "ubuntu" ]
aliases = [ "/questions/1243" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Upgrade wireshark in Ubuntu?](/questions/1243/upgrade-wireshark-in-ubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1243-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to upgrade wireshark in Ubuntu? If so, how can a linux-newby do this?</p></div><div id="question-tags" class="tags-container tags">upgrade ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '10, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/2d5fa0d7685d44e5745aa1d3f635f889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Boonie&#39;s gravatar image" /><p>Boonie<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Boonie has no accepted answers">0%</span></p></div></div><div id="comments-container-1243" class="comments-container"></div><div id="comment-tools-1243" class="comment-tools"></div><div class="clear"></div><div id="comment-1243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="1255"></span>

<div id="answer-container-1255" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1255-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have 1.4.1 running on Ubuntu-based Linux I am not too deep into Linux, but as far as I remember i had like the same issue and got around it by using</p><pre><code> apt-get update
 apt-get upgrade</code></pre><p>and after that manually trying "apt-get install wireshark" and mayby one or two other packages.</p><p>Hope that helps</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '10, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-1255" class="comments-container"><span id="1286"></span><div id="comment-1286" class="comment"><div id="post-1286-score" class="comment-score"></div><div class="comment-text"><p>I just tried that. The result is a few lines of info and one of them is (translated NL to EN): Wireshark is already the latest version.</p><p>But it is not.</p></div><div id="comment-1286-info" class="comment-info"><span class="comment-age">(08 Dec '10, 09:29)</span> Boonie</div></div><span id="1288"></span><div id="comment-1288" class="comment"><div id="post-1288-score" class="comment-score"></div><div class="comment-text"><p>Did you try</p><p>apt-get install wireshark</p><p>apt-get install wireshark-common</p><p>?</p><p>I reinstalled my Linux in a VM to quickly look up the way it worked for me... a regular apt-get upgrade would not install the latest wireshark, while the two commands above did - don't ask me why...</p></div><div id="comment-1288-info" class="comment-info"><span class="comment-age">(08 Dec '10, 12:34)</span> Landi</div></div><span id="1316"></span><div id="comment-1316" class="comment"><div id="post-1316-score" class="comment-score"></div><div class="comment-text"><p>I did. And that responds with "you allready have the latest version"</p></div><div id="comment-1316-info" class="comment-info"><span class="comment-age">(11 Dec '10, 10:01)</span> Boonie</div></div><span id="1374"></span><div id="comment-1374" class="comment"><div id="post-1374-score" class="comment-score"></div><div class="comment-text"><p>Damn, I installed a v10 Ubuntu to test - same issue you have. I was able to install 1.4 from another repository though... So if you want to have 1.4 via apt-get update, i suggest you search for another repo where 1.4 is already packaged and add this to your /etc/apt/sources.list</p><p>See http://ubuntuguide.org/wiki/Ubuntu:Jaunty#Third_party_repositories</p><p>for more details.</p></div><div id="comment-1374-info" class="comment-info"><span class="comment-age">(16 Dec '10, 02:38)</span> Landi</div></div><span id="1398"></span><div id="comment-1398" class="comment"><div id="post-1398-score" class="comment-score"></div><div class="comment-text"><p>That does not look like something a newby understands within an hour or so.</p></div><div id="comment-1398-info" class="comment-info"><span class="comment-age">(19 Dec '10, 01:10)</span> Boonie</div></div></div><div id="comment-tools-1255" class="comment-tools"></div><div class="clear"></div><div id="comment-1255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1248"></span>

<div id="answer-container-1248" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1248-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would expect that the Ubuntu packet upgrade manager can handle this, even though the packages may be a few releases behind the latest stable build available at <a href="http://www.wireshark.org" title="www.wireshark.org">www.wireshark.org</a>. If you need the latest version you can always go for compiling it from scratch, but that is probably a little out of scope for a linux-newbie.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '10, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1248" class="comments-container"><span id="1249"></span><div id="comment-1249" class="comment"><div id="post-1249-score" class="comment-score"></div><div class="comment-text"><p>1.2.11 is the auto installed version. I'd like to go to the 1.4.x version. I do not see a package for linux on the wireshark website. Compiling sounds like something for experts.</p></div><div id="comment-1249-info" class="comment-info"><span class="comment-age">(05 Dec '10, 07:45)</span> Boonie</div></div><span id="1250"></span><div id="comment-1250" class="comment"><div id="post-1250-score" class="comment-score"></div><div class="comment-text"><p>Yes, you'll have to wait for Ubuntu to distribute 1.4, but you can work with 1.2.11 just fine. 1.4 has some improvements but you still can get valid results with 1.2. Compiling isn't totally rocket science but if you're new to Linux it may be a bit too confusing.</p></div><div id="comment-1250-info" class="comment-info"><span class="comment-age">(05 Dec '10, 07:49)</span> Jasper ♦♦</div></div></div><div id="comment-tools-1248" class="comment-tools"></div><div class="clear"></div><div id="comment-1248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1294"></span>

<div id="answer-container-1294" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1294-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your other option is to find a personal/private update that someone has made to suit your Ubuntu release. These are known as PPAs. <a href="http://www.ubuntuupdates.org/pm/wireshark">http://www.ubuntuupdates.org/pm/wireshark</a> lists that there are 1.4.2-2 wireshark PPAs available for Lucid (Ubuntu 10.04) and Maverick (10.10).</p><p>As with anything that is not part of the offical distribution you would have to trust that those guys are doing the right thing. That caveat aside, generally open-source evildoers are found out and extracated pretty quickly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '10, 17:27</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1294" class="comments-container"><span id="1317"></span><div id="comment-1317" class="comment"><div id="post-1317-score" class="comment-score"></div><div class="comment-text"><p>That seem a good option for me. I'm going to try this.</p></div><div id="comment-1317-info" class="comment-info"><span class="comment-age">(11 Dec '10, 10:12)</span> Boonie</div></div><span id="1318"></span><div id="comment-1318" class="comment"><div id="post-1318-score" class="comment-score"></div><div class="comment-text"><p>From your link I found this page. http://www.ubuntuupdates.org/ppa/maverickbleed?dist=maverick</p><p>It says to use these commands:</p><p>sudo add-apt-repository ppa:maverick-bleed/ppa</p><p>sudo apt-get update</p><p>sudo apt-get install &lt;package name=""&gt;</p><p>As package name I used wireshark</p><p>That did some installing but wireshark is still at 1.2.11</p><p>What am I doing wrong?</p><p>My Ubuntu is upgraded to 10.10 so I think I'm using the correct version.</p></div><div id="comment-1318-info" class="comment-info"><span class="comment-age">(11 Dec '10, 10:27)</span> Boonie</div></div><span id="1412"></span><div id="comment-1412" class="comment"><div id="post-1412-score" class="comment-score"></div><div class="comment-text"><p>It seems that the lucid-bleed and maverick-bleed teams have deleted those packages from their repositories. Maybe they had issues with them. You may want to contact them to find out.</p><p>https://launchpad.net/~maverick-bleed/+archive/ppa/+packages</p></div><div id="comment-1412-info" class="comment-info"><span class="comment-age">(20 Dec '10, 15:28)</span> martyvis</div></div></div><div id="comment-tools-1294" class="comment-tools"></div><div class="clear"></div><div id="comment-1294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1611"></span>

<div id="answer-container-1611" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1611-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Jelmer Vernooij's daily builds PPA has wireshark 1.4.2 (at least right now). The home page is at https://launchpad.net/~jelmer/+archive/daily</p><p>Commands:</p><p>sudo apt-add-repository ppa:jelmer/daily</p><p>sudo apt-get update</p><p>sudo apt-get dist-upgrade</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '11, 18:08</strong></p><img src="https://secure.gravatar.com/avatar/f05eda7a9cb8ef639939b88689312fc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="puzzlement&#39;s gravatar image" /><p>puzzlement<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="puzzlement has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jan '11, 18:08</p></div></div><div id="comments-container-1611" class="comments-container"><span id="9609"></span><div id="comment-9609" class="comment"><div id="post-9609-score" class="comment-score"></div><div class="comment-text"><p>I was in touble about wireshark 1.6.5 on ubuntu 10.10 . many errors whiele compiling. too many dependencies and errors installing them. your post did make the difference. thank you very much. The update work and its running now.<br />
</p></div><div id="comment-9609-info" class="comment-info"><span class="comment-age">(18 Mar '12, 12:22)</span> LuizCar</div></div></div><div id="comment-tools-1611" class="comment-tools"></div><div class="clear"></div><div id="comment-1611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

