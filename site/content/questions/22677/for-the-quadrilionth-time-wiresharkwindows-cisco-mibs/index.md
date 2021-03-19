+++
type = "question"
title = "For the quadrilionth time - Wireshark(Windows) Cisco MIBS"
description = '''Please forgive the tone, I am so [expletive] angry right now... For windows the SNMP wireshark page is worthless.  I downloaded the v2 zip from Cisco and unzipped it to c:&#92;users&#92;me&#92;v2 I copied all the .my files from step 1 to c:&#92;users&#92;me&#92;mibs Then with Cygwin I got rid of the .my with &quot;for i in ls;d...'''
date = "2013-07-04T15:15:00Z"
lastmod = "2015-03-31T23:16:00Z"
weight = 22677
keywords = [ "snmp" ]
aliases = [ "/questions/22677" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [For the quadrilionth time - Wireshark(Windows) Cisco MIBS](/questions/22677/for-the-quadrilionth-time-wiresharkwindows-cisco-mibs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22677-score" class="post-score" title="current number of votes">-6</div><span id="post-22677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Please forgive the tone, I am so <del>[expletive]</del> angry right now...</p><p>For windows the SNMP wireshark page is worthless.</p><ol><li>I downloaded the v2 zip from Cisco and unzipped it to c:\users\me\v2</li><li>I copied all the .my files from step 1 to c:\users\me\mibs</li><li>Then with Cygwin I got rid of the .my with "for i in <code>ls</code>;do mv $i `echo $i | awk -F. '{print $1}';done"</li><li>Then I pointed wireshark to c:\users\me\mibs</li></ol><p>I've tried every possible permutation and at this point I'd rather someone <del>[expletive]</del>.</p><p>And NO, I didn't <del>[expletive]</del> compile my own <del>[expletive]</del> version of wireshark for windows, just like 99.9% of windows users, I JUST INSTALLED THE ONE THATS ALREADY COMPILED AND DOWNLOADABLE FROM wireshark.org</p><del>[expletive]</del><p>IS GOING ON HERE!!</p><p>Sorry for the tone</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-snmp" rel="tag" title="see questions tagged &#39;snmp&#39;">snmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '13, 15:15</strong></p><img src="https://secure.gravatar.com/avatar/3227daf2ff52777b80f0b297540739c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daviddionne&#39;s gravatar image" /><p><span>daviddionne</span><br />
<span class="score" title="-11 reputation points">-11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daviddionne has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jul '13, 09:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-22677" class="comments-container"></div><div id="comment-tools-22677" class="comment-tools"></div><div class="clear"></div><div id="comment-22677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="22684"></span>

<div id="answer-container-22684" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22684-score" class="post-score" title="current number of votes">9</div><span id="post-22684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you for your constructive words, they are really motivating me to spend some of my free time this weekend to try to improve Wireshark so it meets your exacting needs for free. Or maybe not.</p><p>You could fix it yourself as the Wireshark project provides all the source, tools and guides to build your own copy of Wireshark, however if that's beyond your capabilities, then you could spend some of your budget and hire someone else with those abilities to do that for you.</p><p>Finally I'll point you to the warranty supplied with Wireshark as detailed in the about menu:</p><pre><code>This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '13, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22684" class="comments-container"></div><div id="comment-tools-22684" class="comment-tools"></div><div class="clear"></div><div id="comment-22684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41076"></span>

<div id="answer-container-41076" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41076-score" class="post-score" title="current number of votes">0</div><span id="post-41076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a good post. I have also been wasting time with MIBs in wireshark all day.</p><p>if you are strugging with wireshark loading mibs, one tip - you may be able to find a quick way to add them to the "smi_modules" file. Saves adding them in the gui.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '15, 23:16</strong></p><img src="https://secure.gravatar.com/avatar/8f11004fd32ec7c6e14445f328ac5555?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sossie07&#39;s gravatar image" /><p><span>sossie07</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sossie07 has no accepted answers">0%</span></p></div></div><div id="comments-container-41076" class="comments-container"></div><div id="comment-tools-41076" class="comment-tools"></div><div class="clear"></div><div id="comment-41076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22678"></span>

<div id="answer-container-22678" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22678-score" class="post-score" title="current number of votes">-4</div><span id="post-22678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So I calmed down and focused...and I think I might get it. Amazing with strace on Linux can do, even for windows. So the little discovery I made was that not only do you have to add the directory but you must also add, ONE BY ONE...BY HAND, the name of every <del>[expletive]</del> mib in the mib modules section of wireshark as well?!</p><p>I made very quick work of this, again with Cygwin and are you people(cace or I guess riverbed now) in a little tiff with cisco?</p><p>This took the most spectacularly dump I've ever seen, I think I could actually smell it. Wireshark died.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '13, 15:38</strong></p><img src="https://secure.gravatar.com/avatar/3227daf2ff52777b80f0b297540739c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daviddionne&#39;s gravatar image" /><p><span>daviddionne</span><br />
<span class="score" title="-11 reputation points">-11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daviddionne has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jul '13, 09:49</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-22678" class="comments-container"><span id="22679"></span><div id="comment-22679" class="comment"><div id="post-22679-score" class="comment-score"></div><div class="comment-text"><p>And I was actually about to try cascade...ive got a few hundred thousand left in my budget this year, figured why not, love wireshark right. well the poopy smell is why not</p></div><div id="comment-22679-info" class="comment-info"><span class="comment-age">(04 Jul '13, 15:40)</span> <span class="comment-user userinfo">daviddionne</span></div></div><span id="22681"></span><div id="comment-22681" class="comment"><div id="post-22681-score" class="comment-score">2</div><div class="comment-text"><p>Uhm, sorry you ran into trouble like this, but it's what happens in a project like Wireshark - some people code a solution as much and as far as they think they need to to be able to solve their problem, and the result is a little awkward to handle for others. That's what can be a downside of open source development, but on the other hand Wireshark is free and the source available - so you could fix it instead of wasting energy on being angry. Yeah, I know, that wasn't what you needed to hear. Sorry again.</p></div><div id="comment-22681-info" class="comment-info"><span class="comment-age">(04 Jul '13, 16:13)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-22678" class="comment-tools"></div><div class="clear"></div><div id="comment-22678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

