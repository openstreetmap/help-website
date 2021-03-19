+++
type = "question"
title = "Wireshark automatically quits the instant I open it on OSX 10.6.7"
description = '''Right now I am using MacOS X with version 10.6.7 and a 2 Ghz Intel Core duo. Every time I double click Wireshark, the program opens and then instantly quits. Can you explain to me what&#x27;s going on? If you need more info please let me know. Thanks.'''
date = "2011-05-17T11:21:00Z"
lastmod = "2012-04-18T11:20:00Z"
weight = 4102
keywords = [ "quits", "mac", "osx", "closes" ]
aliases = [ "/questions/4102" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark automatically quits the instant I open it on OSX 10.6.7](/questions/4102/wireshark-automatically-quits-the-instant-i-open-it-on-osx-1067)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4102-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Right now I am using MacOS X with version 10.6.7 and a 2 Ghz Intel Core duo. Every time I double click Wireshark, the program opens and then instantly quits. Can you explain to me what's going on? If you need more info please let me know. Thanks.</p></div><div id="question-tags" class="tags-container tags">quits mac osx closes</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '11, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/e13fc44178f7bfc9bcf9ce8c28110788?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="redelman431&#39;s gravatar image" /><p>redelman431<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="redelman431 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Apr '12, 12:25</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-4102" class="comments-container"><span id="4103"></span><div id="comment-4103" class="comment"><div id="post-4103-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark are you using?</p></div><div id="comment-4103-info" class="comment-info"><span class="comment-age">(17 May '11, 12:38)</span> multipleinte...</div></div><span id="4104"></span><div id="comment-4104" class="comment"><div id="post-4104-score" class="comment-score"></div><div class="comment-text"><p>version 1.4.6</p></div><div id="comment-4104-info" class="comment-info"><span class="comment-age">(17 May '11, 13:45)</span> redelman431</div></div><span id="4107"></span><div id="comment-4107" class="comment"><div id="post-4107-score" class="comment-score"></div><div class="comment-text"><p>@redelman431 Can you try 1.6.0rc1?</p></div><div id="comment-4107-info" class="comment-info"><span class="comment-age">(17 May '11, 15:24)</span> Gerald Combs ♦♦</div></div><span id="4110"></span><div id="comment-4110" class="comment"><div id="post-4110-score" class="comment-score"></div><div class="comment-text"><p>Same thing happens.</p></div><div id="comment-4110-info" class="comment-info"><span class="comment-age">(17 May '11, 15:37)</span> redelman431</div></div><span id="4126"></span><div id="comment-4126" class="comment not_top_scorer"><div id="post-4126-score" class="comment-score"></div><div class="comment-text"><p>Are you able to run tshark from the command-line? What happens if you try to start Wireshark from the command-line - do you get any error messages printed out?</p></div><div id="comment-4126-info" class="comment-info"><span class="comment-age">(18 May '11, 19:10)</span> cmaynard ♦♦</div></div><span id="4129"></span><div id="comment-4129" class="comment"><div id="post-4129-score" class="comment-score">1</div><div class="comment-text"><p>Your console log should be capturing these crashes (<code>/Applications/Utilities/Console</code>). Also check for Wireshark crash reports in <code>~/Library/Logs/DiagnosticReports/wireshark-bin_*.crash</code>.</p></div><div id="comment-4129-info" class="comment-info"><span class="comment-age">(18 May '11, 20:12)</span> helloworld</div></div><span id="10290"></span><div id="comment-10290" class="comment not_top_scorer"><div id="post-10290-score" class="comment-score"></div><div class="comment-text"><p>This is a common problem and so far there are no good answers. The best answer I have seen about this is: <a href="https://discussions.apple.com/thread/3873212?start=0&amp;tstart=0">https://discussions.apple.com/thread/3873212?start=0&amp;tstart=0</a> at the bottom he says: Easiest? Contact the folks that are administering the Wireshark download kit for OS X, and tell them that it's broken, and pass along the errors you're getting.</p><p>The Wireshark installer package deals with the installation itself; with locating the tools in the expected places. (Wireshark is clearly not set up as a Mac application bundle - which you could then drag where you want ...</p></div><div id="comment-10290-info" class="comment-info"><span class="comment-age">(19 Apr '12, 10:00)</span> WantaKnow</div></div><span id="10314"></span><div id="comment-10314" class="comment not_top_scorer"><div id="post-10314-score" class="comment-score"></div><div class="comment-text"><p>There's no "this" here - there's more than one problem. The problem redelman431's seeing might be the comment "libfreetype is too old" problem, or it might be "running the 64-bit build on a 32-bit machine".</p><p>The fastest way to try to deal with the "libfreetype is too old" problem is to update to 10.6.8 <em>and</em> install all the security updates (keep running Software Update until it has no updates for you); that could get things going in a relatively short period of time.</p></div><div id="comment-10314-info" class="comment-info"><span class="comment-age">(19 Apr '12, 15:25)</span> Guy Harris ♦♦</div></div><span id="10315"></span><div id="comment-10315" class="comment not_top_scorer"><div id="post-10315-score" class="comment-score"></div><div class="comment-text"><p>And, actually, Wireshark <em>is</em> an application bundle that you can drag elsewhere - I just did that (dragged it from <code>/Applications</code> to my home directory) and it worked. The bundle doesn't include libfreetype, but it doesn't include libSystem either; it relies on the OS to supply that. (If <a href="https://discussions.apple.com/message/18125733#18125733">MrHoffman thinks that only drag-install apps are application bundles</a>, he's mistaken.)</p><p>The problem is that, as per <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5937">bug 5937</a>, Wireshark is built against the library versions on the buildbot.</p></div><div id="comment-10315-info" class="comment-info"><span class="comment-age">(19 Apr '12, 15:30)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-4102" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-4102-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10245"></span>

<div id="answer-container-10245" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10245-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>try installing XCode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '12, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/19171d28ed2aa1aed6b5586a13308a57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhishek&#39;s gravatar image" /><p>Abhishek<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhishek has no accepted answers">0%</span></p></div></div><div id="comments-container-10245" class="comments-container"></div><div id="comment-tools-10245" class="comment-tools"></div><div class="clear"></div><div id="comment-10245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10250"></span>

<div id="answer-container-10250" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10250-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you install this from one of the .dmg's on <a href="http://wireshark.org">wireshark.org</a>? If so, did you install the 32-bit Leopard version or the 64-bit Snow Leopard version? If you have a Core Duo processor, rather than a Core 2 or a Core i{3,5,7} processor, you have a 32-bit processor and the 64-bit version will not run, so you have to install the 32-bit Leopard version even though your machine is running Snow Leopard (we aren't building a 64-bit Leopard version).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '12, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10250" class="comments-container"></div><div id="comment-tools-10250" class="comment-tools"></div><div class="clear"></div><div id="comment-10250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

