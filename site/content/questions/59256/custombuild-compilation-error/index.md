+++
type = "question"
title = "CUSTOMBUILD : compilation error"
description = '''I have successfully build wireshark 2.2.1 in the same machine with same development Environment. Everything was perfect. Recently I wanted to buuild wireshark 2.2.4 and was unsuccesfull and ist showing These Errors. I have tried with 2.2.2 source code too. But These same Errors appear again! What co...'''
date = "2017-02-06T06:33:00Z"
lastmod = "2017-02-14T07:49:00Z"
weight = 59256
keywords = [ "build_error", "compilation", "wireshark-2.0" ]
aliases = [ "/questions/59256" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [CUSTOMBUILD : compilation error](/questions/59256/custombuild-compilation-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59256-score" class="post-score" title="current number of votes">0</div><span id="post-59256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have successfully build wireshark 2.2.1 in the same machine with same development Environment. Everything was perfect. Recently I wanted to buuild wireshark 2.2.4 and was unsuccesfull and ist showing These Errors. I have tried with 2.2.2 source code too. But These same Errors appear again! What could be the case? Thanks</p><pre><code>         &quot;C:\Temp\_temp\Development\wsbuild32\Wireshark.sln&quot; (Standardziel) (1) -&gt;
   &quot;C:\Temp\_temp\Development\wsbuild32\docbook\developer_guide_chm.vcxproj.metaproj&quot; (Standardziel) (16) -&gt;
   &quot;C:\Temp\_temp\Development\wsbuild32\docbook\developer_guide_chm.vcxproj&quot; (Standardziel) (118) -&gt;
   (CustomBuild Ziel) -&gt; 
     CUSTOMBUILD : compilation error : file C:/Temp/_temp/htmlhelp.xsl line 19 element import [C:\Temp\_temp\Development\wsbuild32\docbook\developer_guide_chm.vcxproj]
     CUSTOMBUILD : compilation error : file C:/Temp/_temp/htmlhelp.xsl line 20 element include [C:\Temp\_temp\Development\wsbuild32\docbook\developer_guide_chm.vcxproj]

   &quot;C:\Temp\_temp\Development\wsbuild32\Wireshark.sln&quot; (Standardziel) (1) -&gt;
   &quot;C:\Temp\_temp\Development\wsbuild32\docbook\user_guide_chm.vcxproj.metaproj&quot; (Standardziel) (65) -&gt;
   &quot;C:\Temp\_temp\Development\wsbuild32\docbook\user_guide_chm.vcxproj&quot; (Standardziel) (116) -&gt;
     CUSTOMBUILD : compilation error : file C:/Temp/_temp/htmlhelp.xsl line 19 element import [C:\Temp\_temp\Development\wsbuild32\docbook\user_guide_chm.vcxproj]
     CUSTOMBUILD : compilation error : file C:/Temp/_temp/htmlhelp.xsl line 20 element include [C:\Temp\_temp\Development\wsbuild32\docbook\user_guide_chm.vcxproj]</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span> <span class="post-tag tag-link-compilation" rel="tag" title="see questions tagged &#39;compilation&#39;">compilation</span> <span class="post-tag tag-link-wireshark-2.0" rel="tag" title="see questions tagged &#39;wireshark-2.0&#39;">wireshark-2.0</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '17, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/a908c48c60a3ba8f08a762a9cb58268f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xaheen&#39;s gravatar image" /><p><span>xaheen</span><br />
<span class="score" title="71 reputation points">71</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xaheen has one accepted answer">50%</span></p></div></div><div id="comments-container-59256" class="comments-container"></div><div id="comment-tools-59256" class="comment-tools"></div><div class="clear"></div><div id="comment-59256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59406"></span>

<div id="answer-container-59406" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59406-score" class="post-score" title="current number of votes">0</div><span id="post-59406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="xaheen has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have filnally got somewhere with the issue - This is because of the Company's Firewall. But Dont worry, it dosent bother at all .i have successfully compiled a plugin while These 4 Errors were there. The plugin functions perfectly. So, just avoid These Errors if you are having them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '17, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/a908c48c60a3ba8f08a762a9cb58268f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xaheen&#39;s gravatar image" /><p><span>xaheen</span><br />
<span class="score" title="71 reputation points">71</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xaheen has one accepted answer">50%</span></p></div></div><div id="comments-container-59406" class="comments-container"><span id="59408"></span><div id="comment-59408" class="comment"><div id="post-59408-score" class="comment-score">1</div><div class="comment-text"><p>The files aren't required to build a plugin, only to create documentation for a full installer.</p></div><div id="comment-59408-info" class="comment-info"><span class="comment-age">(14 Feb '17, 07:49)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-59406" class="comment-tools"></div><div class="clear"></div><div id="comment-59406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59257"></span>

<div id="answer-container-59257" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59257-score" class="post-score" title="current number of votes">1</div><span id="post-59257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's likely that there is an error in a file that's not getting rebuilt as there's no changes to the source that generates that file.</p><p>You can try to force a rebuild by adding a <code>"/t:Rebuild"</code> to the end of your msbuild command, or take the brute force approach of deleting your build directory (wsbuild32), creating a new one and running the cmake and msbuild steps again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '17, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-59257" class="comments-container"><span id="59258"></span><div id="comment-59258" class="comment"><div id="post-59258-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@grahamb</span>, I have actually totally cleaned and rebuilt the whole wireshark 3 times. everytime the same Problem...</p></div><div id="comment-59258-info" class="comment-info"><span class="comment-age">(06 Feb '17, 07:05)</span> <span class="comment-user userinfo">xaheen</span></div></div><span id="59259"></span><div id="comment-59259" class="comment"><div id="post-59259-score" class="comment-score">1</div><div class="comment-text"><p>Looking in more depth at the error messages the path seems a little odd, <code>C:/Temp/_temp/htmlhelp.xsl</code>, this seems to be one directory above your source tree.</p><p>I have multiple htmlhelp.xsl files in my Cygwin install, but none of them outside there. What's your Cygwin install path, and what else is in <code>C:\Temp\_temp</code></p></div><div id="comment-59259-info" class="comment-info"><span class="comment-age">(06 Feb '17, 07:25)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-59257" class="comment-tools"></div><div class="clear"></div><div id="comment-59257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

