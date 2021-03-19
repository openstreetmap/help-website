+++
type = "question"
title = "My dissector which was compiled with 1.8, doesn&#x27;t work on official 1.8"
description = '''Hey, I compiled (VS2010) my dissector with the 1.8 trunk release and even tried it the the 1.8.4 official source release but it still doesn&#x27;t work with the official 1.8.4 release. The dissector works only for the release that I build him for: If I build it with trunk 1.8, It only works for my own bu...'''
date = "2012-12-15T07:18:00Z"
lastmod = "2012-12-17T01:25:00Z"
weight = 16928
keywords = [ "dissector", "wireshark" ]
aliases = [ "/questions/16928" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [My dissector which was compiled with 1.8, doesn't work on official 1.8](/questions/16928/my-dissector-which-was-compiled-with-18-doesnt-work-on-official-18)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16928-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, I compiled (VS2010) my dissector with the 1.8 trunk release and even tried it the the 1.8.4 official source release but it still doesn't work with the official 1.8.4 release.</p><p>The dissector works only for the release that I build him for: If I build it with trunk 1.8, It only works for my own build.</p><p>The dissector is a plugin</p><p>The build works fine, afterwards I copy the .dll to the plugin\version dir of the official release and I execute the official release, then I get an error message about my dissector</p><p>The error message:</p><blockquote><p>"Couldn't load module C:\Program Files\Wireshark\plugins\1.8.4\my_plugin.dll: `C:\Program Files\Wireshark\plugins\1.8.4\my_plugin.dll': %1 is not a valid Win32 application."</p></blockquote><p>edit: I tried to see if the problem is in my dissector, or in they way I build... I took a working plugin "gryphon" and built it, copied it to the official wireshark\plugins\1.8.4\ and it gives me the same error. So I guess something is wrong with my build...</p><p>Does anyone have any suggestions?</p><p>Thanks ahead</p></div><div id="question-tags" class="tags-container tags">dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '12, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/b7ccaef1113111fc5cb2bb2a0d866a4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hudac&#39;s gravatar image" /><p>hudac<br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hudac has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Dec '12, 01:06</p></div></div><div id="comments-container-16928" class="comments-container"><span id="16929"></span><div id="comment-16929" class="comment"><div id="post-16929-score" class="comment-score"></div><div class="comment-text"><p>You'll need to provide more information before anyone can answer your question.</p><p>What doesn't work ? Build ? Error messages ? etc.</p><p>What kind of dissector: Plugin ? Built-in ?</p><p>For what release does the dissector work with ?</p></div><div id="comment-16929-info" class="comment-info"><span class="comment-age">(15 Dec '12, 07:25)</span> Bill Meier ♦♦</div></div><span id="16930"></span><div id="comment-16930" class="comment"><div id="post-16930-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the comment. The dissector works only for the release that I build him for: If I build it with trunk 1.8, It only works for my own build.</p><p>The dissector is a plugin</p><p>The build works fine, afterwards I copy the .dll to the plugin\version dir of the official release and I execute the official release, then I get an error message about my dissector (unfortunately I will be able to write the error message only on Monday...)</p></div><div id="comment-16930-info" class="comment-info"><span class="comment-age">(15 Dec '12, 07:57)</span> hudac</div></div><span id="16960"></span><div id="comment-16960" class="comment"><div id="post-16960-score" class="comment-score"></div><div class="comment-text"><p>can you post your compiled version of the <strong>gryphon</strong> plugin somewhere?</p></div><div id="comment-16960-info" class="comment-info"><span class="comment-age">(17 Dec '12, 01:55)</span> Kurt Knochner ♦</div></div><span id="16966"></span><div id="comment-16966" class="comment"><div id="post-16966-score" class="comment-score"></div><div class="comment-text"><p>Thanks, my mistake was that I thought I built for win64, while I built for win32... I tried to run it on win64 and it didn't work...</p></div><div id="comment-16966-info" class="comment-info"><span class="comment-age">(17 Dec '12, 03:24)</span> hudac</div></div></div><div id="comment-tools-16928" class="comment-tools"></div><div class="clear"></div><div id="comment-16928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16958"></span>

<div id="answer-container-16958" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16958-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you built your plugin for Win64 and are now running a 32 bit version of Wireshark? You'll need to match the bit size of Wireshark and the plugin.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '12, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-16958" class="comments-container"><span id="16959"></span><div id="comment-16959" class="comment"><div id="post-16959-score" class="comment-score"></div><div class="comment-text"><p>I built it for win64, and I'm running 64bit version of wireshark...</p></div><div id="comment-16959-info" class="comment-info"><span class="comment-age">(17 Dec '12, 01:29)</span> hudac</div></div><span id="16963"></span><div id="comment-16963" class="comment"><div id="post-16963-score" class="comment-score"></div><div class="comment-text"><p>Can you post the output of <code>dumpbin /headers path\to\your\dll</code>?</p></div><div id="comment-16963-info" class="comment-info"><span class="comment-age">(17 Dec '12, 02:56)</span> grahamb ♦</div></div><span id="16965"></span><div id="comment-16965" class="comment"><div id="post-16965-score" class="comment-score"></div><div class="comment-text"><p>Thanks, my mistake was that I thought I built for win64, while I built for win32... I tried to run it on win64 and it didn't work...</p></div><div id="comment-16965-info" class="comment-info"><span class="comment-age">(17 Dec '12, 03:24)</span> hudac</div></div><span id="16970"></span><div id="comment-16970" class="comment"><div id="post-16970-score" class="comment-score"></div><div class="comment-text"><p>If the answer solved your issue can you accept it for the benefit of other users by clicking the checkmark icon?</p></div><div id="comment-16970-info" class="comment-info"><span class="comment-age">(17 Dec '12, 03:59)</span> grahamb ♦</div></div></div><div id="comment-tools-16958" class="comment-tools"></div><div class="clear"></div><div id="comment-16958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16931"></span>

<div id="answer-container-16931" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16931-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Once you post the error message, someone may be able to identify the specific problem.</p><p>That being said, a Google search for '<code>site:wireshark.org plugin "1.8"</code>' gives a number of hits which may be worth investigating.</p><p>As noted elsewhere [<a href="http://ask.wireshark.org/questions/13043/plugin-not-loading">plugin not loading</a>]</p><p>"Wireshark does not guarantee that plugins built against a given major release (such as 1.4.x, for various values of x) will continue to work with later major releases (such as 1.6.x or 1.8.x, for various values of x)."</p><p>It' certainly possible that you will need coding changes in your dissector for use with Wireshark 1.8 (altho that may not be the actual problem since you say it works with your 1.8 build).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '12, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Dec '12, 08:22</p></div></div><div id="comments-container-16931" class="comments-container"><span id="16953"></span><div id="comment-16953" class="comment"><div id="post-16953-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your comment, I added the error message.. It will be very helpful if you could look at it</p></div><div id="comment-16953-info" class="comment-info"><span class="comment-age">(16 Dec '12, 22:25)</span> hudac</div></div></div><div id="comment-tools-16931" class="comment-tools"></div><div class="clear"></div><div id="comment-16931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

