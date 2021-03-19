+++
type = "question"
title = "Wireshark application termination"
description = '''Hello All, I hard-coded some changes to preferences through epan/prefs.c file. I also removed the preferences file present in C:&#92;Doc &amp;amp; Settings&#92;..&#92;preferences. I was successful in reflecting the needed changes, but Wireshark aborts immediately if i click on the Cancel button of the Edit-&amp;gt;Pref...'''
date = "2011-09-12T05:28:00Z"
lastmod = "2011-09-13T02:51:00Z"
weight = 6279
keywords = [ "development" ]
aliases = [ "/questions/6279" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark application termination](/questions/6279/wireshark-application-termination)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6279-score" class="post-score" title="current number of votes">0</div><span id="post-6279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I hard-coded some changes to <code>preferences</code> through <code>epan/prefs.c</code> file. I also removed the <code>preferences</code> file present in <code>C:\Doc &amp; Settings\..\preferences</code>. I was successful in reflecting the needed changes, but Wireshark aborts immediately if i click on the Cancel button of the <strong>Edit-&gt;Preferences</strong> dialog box or <strong>File-&gt;Quit</strong> option. Kindly resolve this issue.</p><p>Thanks, Regards, Prashanth</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '11, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p><span>Terrestrial ...</span><br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Sep '11, 23:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6279" class="comments-container"><span id="6286"></span><div id="comment-6286" class="comment"><div id="post-6286-score" class="comment-score">4</div><div class="comment-text"><p>You'll probably need to use a debugger to see what's going on....</p></div><div id="comment-6286-info" class="comment-info"><span class="comment-age">(12 Sep '11, 07:48)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-6279" class="comment-tools"></div><div class="clear"></div><div id="comment-6279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6292"></span>

<div id="answer-container-6292" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6292-score" class="post-score" title="current number of votes">1</div><span id="post-6292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Terrestrial shark has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at all the places where you made changes and pay attention to memory allocations and frees, you may have freed memory that will be freed later on by GTK.</p><p>Apart from that, it's almost impossible to resolve your issue as we do not have the code to look at, nor debugging output to work with. So I'm afraid I will have to send you home to do some homework ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '11, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6292" class="comments-container"><span id="6300"></span><div id="comment-6300" class="comment"><div id="post-6300-score" class="comment-score"></div><div class="comment-text"><p>How to use the Debugger? Where can i Find it?</p></div><div id="comment-6300-info" class="comment-info"><span class="comment-age">(12 Sep '11, 21:30)</span> <span class="comment-user userinfo">Terrestrial ...</span></div></div><span id="6304"></span><div id="comment-6304" class="comment"><div id="post-6304-score" class="comment-score">1</div><div class="comment-text"><p>Read this page http://wiki.wireshark.org/Development/Tips?highlight=%28debugger%29</p></div><div id="comment-6304-info" class="comment-info"><span class="comment-age">(12 Sep '11, 22:39)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="6306"></span><div id="comment-6306" class="comment"><div id="post-6306-score" class="comment-score"></div><div class="comment-text"><p>I have used the debugger. The warning is: 11:34:07 Warn C:Documents and SettingsadminApplication DataWiresharkpreferences line 134: Syntax error in preference column.format (applying your preferences once should remove this warning)</p></div><div id="comment-6306-info" class="comment-info"><span class="comment-age">(12 Sep '11, 23:05)</span> <span class="comment-user userinfo">Terrestrial ...</span></div></div><span id="6307"></span><div id="comment-6307" class="comment"><div id="post-6307-score" class="comment-score">1</div><div class="comment-text"><p>Start Wireshark in the debugger, and then cause the crash (which sounds easily reproducible for you). The debugger should break at/near the crash point.</p></div><div id="comment-6307-info" class="comment-info"><span class="comment-age">(12 Sep '11, 23:18)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="6315"></span><div id="comment-6315" class="comment"><div id="post-6315-score" class="comment-score"></div><div class="comment-text"><p>I have totally 32 Columns to hardcode. When i add upto 30 Columns its not getting crashed but if i the other two columns too i can see the crashing of the wireshark. How many number of columns can wireshark accept?</p></div><div id="comment-6315-info" class="comment-info"><span class="comment-age">(13 Sep '11, 01:23)</span> <span class="comment-user userinfo">Terrestrial ...</span></div></div><span id="6316"></span><div id="comment-6316" class="comment not_top_scorer"><div id="post-6316-score" class="comment-score"></div><div class="comment-text"><p>Thanks for every one!! I have resolved it. Its just due to the mismatch of Column type and Custom_field values.</p></div><div id="comment-6316-info" class="comment-info"><span class="comment-age">(13 Sep '11, 02:51)</span> <span class="comment-user userinfo">Terrestrial ...</span></div></div></div><div id="comment-tools-6292" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-6292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

