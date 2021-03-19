+++
type = "question"
title = "build with dissector plugin fails in Windows"
description = '''Hi, I have recently built a plugin dissector successfully in Linux. Now, I&#x27;m trying to compile and build the same plugin in Win environment. I have managed to setup my code environment and msbuild was executed successfully (without my plugin) However, once I add my dissector to my project and try to...'''
date = "2017-03-03T06:18:00Z"
lastmod = "2017-03-05T23:32:00Z"
weight = 59828
keywords = [ "windows", "build", "dissector", "error", "plugin" ]
aliases = [ "/questions/59828" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [build with dissector plugin fails in Windows](/questions/59828/build-with-dissector-plugin-fails-in-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59828-score" class="post-score" title="current number of votes">0</div><span id="post-59828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have recently built a plugin dissector successfully in Linux. Now, I'm trying to compile and build the same plugin in Win environment. I have managed to setup my code environment and msbuild was executed successfully (without my plugin)</p><p>However, once I add my dissector to my project and try to build again, I get the following error:</p><p>Build FAILED.</p><pre><code>   &quot;C:\Development\wsbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (default target) (2) -&gt;
   &quot;C:\Development\wsbuild64\plugins\map\map.vcxproj.metaproj&quot; (default target) (62) -&gt;
   &quot;C:\Development\wsbuild64\plugins\map\map.vcxproj&quot; (default target) (146) -&gt;
   (CustomBuild target) -&gt;
     C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\wsbuild64\plugins\map\map.vcxproj]

0 Warning(s)
1 Error(s)</code></pre><p>I've gone through the procedure in README.plugins step by step. I'm using the 'custom extension' option. What am I missing here?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '17, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/0cc0debf9f6cf8601913135a0d0ec76b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gerolima&#39;s gravatar image" /><p><span>gerolima</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gerolima has one accepted answer">50%</span></p></div></div><div id="comments-container-59828" class="comments-container"><span id="59832"></span><div id="comment-59832" class="comment"><div id="post-59832-score" class="comment-score"></div><div class="comment-text"><p>in fact this is what I get:</p><pre><code>Generating plugin.c
110&gt;  Traceback (most recent call last):
110&gt;    File &quot;C:\Development\wireshark\tools\make-dissector-reg.py&quot;, line 156, in &lt;module&gt;
110&gt;      contents = file.read()
110&gt;    File &quot;C:\Python36\lib\encodings\cp1253.py&quot;, line 23, in decode
110&gt;      return codecs.charmap_decode(input,self.errors,decoding_table)[0]
110&gt;  UnicodeDecodeError: &#39;charmap&#39; codec can&#39;t decode byte 0x9c in position 43319: character maps to &lt;undefined&gt;
110&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1.</code></pre><p>Is this a python problem? (i'm using python 3)</p></div><div id="comment-59832-info" class="comment-info"><span class="comment-age">(03 Mar '17, 10:21)</span> <span class="comment-user userinfo">gerolima</span></div></div><span id="59850"></span><div id="comment-59850" class="comment"><div id="post-59850-score" class="comment-score"></div><div class="comment-text"><p>This sounds like you have an odd character in your source file that causes the code page issues. As Python3 has rearranged the deckchairs with regard to Unicode as default for strings this is unlikely to be an issue for Python2.</p><p>What is the character you have in your source file (looks to be 0x9c at position 43319)?</p></div><div id="comment-59850-info" class="comment-info"><span class="comment-age">(04 Mar '17, 11:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-59828" class="comment-tools"></div><div class="clear"></div><div id="comment-59828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59866"></span>

<div id="answer-container-59866" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59866-score" class="post-score" title="current number of votes">0</div><span id="post-59866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gerolima has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>I had a look again as grahamb suggested. The problem was the following part</p><pre><code>static const value_string fan[] = {
        {0x00, &quot;FAN Off, ODU stops the fan (troubleshooting)&quot;},
        {0x01, &quot;FAN on, ODU runs the FAN at the speed specified in the &quot;FAN Speed&quot; parameter&quot;},
        {0x02, &quot;reserved for ODU internally&quot;}, };</code></pre><p>The double quotes inside the double quotes for the string created the problem. (ie. "FAN Speed")</p><p>many thanks for the support.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '17, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/0cc0debf9f6cf8601913135a0d0ec76b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gerolima&#39;s gravatar image" /><p><span>gerolima</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gerolima has one accepted answer">50%</span></p></div></div><div id="comments-container-59866" class="comments-container"></div><div id="comment-tools-59866" class="comment-tools"></div><div class="clear"></div><div id="comment-59866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59843"></span>

<div id="answer-container-59843" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59843-score" class="post-score" title="current number of votes">0</div><span id="post-59843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I was able to overcome this issue, by adding in the make-dissector-reg.py, in the open(file) function an extra argument for the encoding so that the script doesn't use the system's default encoding. Please consider this as a dirty solution</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '17, 00:38</strong></p><img src="https://secure.gravatar.com/avatar/0cc0debf9f6cf8601913135a0d0ec76b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gerolima&#39;s gravatar image" /><p><span>gerolima</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gerolima has one accepted answer">50%</span></p></div></div><div id="comments-container-59843" class="comments-container"></div><div id="comment-tools-59843" class="comment-tools"></div><div class="clear"></div><div id="comment-59843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

