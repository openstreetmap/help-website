+++
type = "question"
title = "unable run wireshark after install"
description = '''I have built wireshark 1.7.0, lua ver lua5.1.dll from win7 OS, 32 bit installer using VS 2008. have set target to win32. After installation when run on a m/c without VS 2008 , it throws an error &quot;unable to start application &quot; with error code 0xc150002 and terminates. It runs properly on a m/c with V...'''
date = "2012-09-21T03:13:00Z"
lastmod = "2012-09-21T04:01:00Z"
weight = 14420
keywords = [ "installer" ]
aliases = [ "/questions/14420" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [unable run wireshark after install](/questions/14420/unable-run-wireshark-after-install)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14420-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have built wireshark 1.7.0, lua ver lua5.1.dll from win7 OS, 32 bit installer using VS 2008. have set target to win32. After installation when run on a m/c without VS 2008 , it throws an error "unable to start application " with error code 0xc150002 and terminates. It runs properly on a m/c with VS 2008</p><p>Please answer 1) can we build an installer on win7 , a 32 bit installer? 2) what should be done resolve error.</p><p>Your early inputs will be appreciated</p></div><div id="question-tags" class="tags-container tags">installer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '12, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/58a0b723193dca931ba99c422c8a0e74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krithiga&#39;s gravatar image" /><p>krithiga<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krithiga has no accepted answers">0%</span></p></div></div><div id="comments-container-14420" class="comments-container"></div><div id="comment-tools-14420" class="comment-tools"></div><div class="clear"></div><div id="comment-14420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14424"></span>

<div id="answer-container-14424" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14424-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>1.7.0 is a development version and as such may have issues. I regularly build 32bit wireshark installers on win7 (albeit x64) with no issues. Try a stable version such as 1.8.2.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '12, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-14424" class="comments-container"><span id="14427"></span><div id="comment-14427" class="comment"><div id="post-14427-score" class="comment-score"></div><div class="comment-text"><p>Thanks Grahamb for that quick response. will try with 1.8.2 and will get back in case of issues if any</p></div><div id="comment-14427-info" class="comment-info"><span class="comment-age">(21 Sep '12, 04:28)</span> krithiga</div></div><span id="14537"></span><div id="comment-14537" class="comment"><div id="post-14537-score" class="comment-score"></div><div class="comment-text"><p>I had tried with ver 1.8.2 without my changes. I could run successfully from the 32 bit installer compiled on my win 7 m/c for 32 bit installer. I had set the target platform to win32 explicitly in config.nmake file as below</p><p>WIRESHARK_TARGET_PLATFORM=win32</p><p>But with my changes, i am unable to run successfully using the generated installer. Getting same error "unable to start application " with error code 0xc150002 ".</p><p>I have added logs in ui\gtk\main.c and but it appears that even main() is not being entered.</p><p>Any early input will help me lot</p></div><div id="comment-14537-info" class="comment-info"><span class="comment-age">(26 Sep '12, 03:28)</span> krithiga</div></div><span id="14538"></span><div id="comment-14538" class="comment"><div id="post-14538-score" class="comment-score"></div><div class="comment-text"><p>Can you run your modified version from the build directory, i.e. <code>your build dir\wireshark-gtk2</code>? This cuts out the installer part and just runs the newly built copy.</p><p>What are your changes, i.e. have you modified an existing dissector, or have you added a new one that maybe has a dependency on another dll that isn't being included in the installer?</p></div><div id="comment-14538-info" class="comment-info"><span class="comment-age">(26 Sep '12, 03:59)</span> grahamb ♦</div></div><span id="14543"></span><div id="comment-14543" class="comment"><div id="post-14543-score" class="comment-score"></div><div class="comment-text"><p>Sonds lika a problem with vcredist or something like that. Can you use VS2010?</p></div><div id="comment-14543-info" class="comment-info"><span class="comment-age">(26 Sep '12, 06:46)</span> Anders ♦</div></div><span id="14545"></span><div id="comment-14545" class="comment"><div id="post-14545-score" class="comment-score"></div><div class="comment-text"><p>Thanks graham for the pointers. Yes i have added a new dissector in plugin directory and it also registers preferences. It is crashing while loading preference of encap type WTAP_ENCAP_USER0. Also have increased the num cols from 7 to 8 in prefs.c file and also added have added new custom columns.</p><h1 id="define-def_num_cols-7--8">define DEF_NUM_COLS 7--&gt;8</h1><p>on code review observed that in for loop memory allocation is not as per columns definition.</p><p>have updated code and building it. should work now</p><p>will get back if there is still issue if any</p></div><div id="comment-14545-info" class="comment-info"><span class="comment-age">(26 Sep '12, 07:29)</span> krithiga</div></div></div><div id="comment-tools-14424" class="comment-tools"></div><div class="clear"></div><div id="comment-14424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

