+++
type = "question"
title = "are there c# API&#x27;s to process a directory of many WireShark capture files programmatically?"
description = '''Scenario: my dedicated web server gets little traffic daily which is not surprising because there is little to offer, for example, in the last 20 minutes, there was approximately 0.001% of its monthly included bandwidth usage quota. monthly, my bandwidth usage rarely exceeds 10%, however, yesterday,...'''
date = "2014-05-24T09:17:00Z"
lastmod = "2014-05-28T13:46:00Z"
weight = 33037
keywords = [ "c#", "api", "batch", "analysis" ]
aliases = [ "/questions/33037" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [are there c\# API's to process a directory of many WireShark capture files programmatically?](/questions/33037/are-there-c-apis-to-process-a-directory-of-many-wireshark-capture-files-programmatically)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33037-score" class="post-score" title="current number of votes">0</div><span id="post-33037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Scenario:</p><p>my dedicated web server gets little traffic daily which is not surprising because there is little to offer, for example, in the last 20 minutes, there was approximately 0.001% of its monthly included bandwidth usage quota.</p><p>monthly, my bandwidth usage rarely exceeds 10%, however, yesterday, May 23rd, there was over 1% (11.8 GB) in just over 15 hours.</p><p>i launched WireShark and set it to save a new capture file every 10MB or 10 minutes ... most of the captured files were 10MB; in about 92 minutes WireShark saved 140 10MB capture files.</p><p>analyzing these files manually will take me a very long time ...</p><p>QUESTION</p><p>are there c# API's that i can use to code a programmatic solution?</p><p>types of analysis that i'd like to code include number of times a given ip address occurred, ranked by most frequent to least frequent, protocol distribution, ip with protocol, source bytes, destination bytes, et cetera.</p><p>Thank you. Gerry</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-batch" rel="tag" title="see questions tagged &#39;batch&#39;">batch</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '14, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/19484af15d71029638215d497a3daa83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gerryLowry&#39;s gravatar image" /><p><span>gerryLowry</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gerryLowry has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 May '14, 09:19</strong> </span></p></div></div><div id="comments-container-33037" class="comments-container"><span id="33039"></span><div id="comment-33039" class="comment"><div id="post-33039-score" class="comment-score"></div><div class="comment-text"><p>my searches missed this: <a href="http://ask.wireshark.org/questions/10923/using-wireshark-libraries-in-c">http://ask.wireshark.org/questions/10923/using-wireshark-libraries-in-c</a> and another link that points to it. what i hope for is an simple c# API that already wraps libwireshark.dll and/or avoids complexity ... if libwireshark.dll is the only way, i'd like at least to locate documentation dealing with the file structure of WireShark's capture files ... my goal is not to recreate WireShark ... rather, i simply want, in a timely fashion, to analyze the data already captured yesterday.</p></div><div id="comment-33039-info" class="comment-info"><span class="comment-age">(24 May '14, 09:58)</span> <span class="comment-user userinfo">gerryLowry</span></div></div></div><div id="comment-tools-33037" class="comment-tools"></div><div class="clear"></div><div id="comment-33037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33042"></span>

<div id="answer-container-33042" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33042-score" class="post-score" title="current number of votes">1</div><span id="post-33042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's nothing directly for using Wireshark from C#, it 's a native C application so you can use <a href="http://msdn.microsoft.com/en-us/library/ms235282.aspx">PInvoke</a> to call it, but note that libwireshark isn't particularly designed for external use.</p><p>There is <a href="http://pcapdotnet.codeplex.com/">Pcap.Net</a> which is mainly for working with Pcap files but it does have some packet dissection.</p><p>I think you would get results quicker, i.e. with less effort, using tshark to process the pcaps and then either use C# or a script language such as PowerShell to process the text output from tshark.<br />
</p><p>Note that <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a> can already provide some of the analysis you are after, have a look at the <code>-z,conv,...</code> option</p><p>Edit: Fixed link to tshark man page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '14, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 May '14, 14:22</strong> </span></p></div></div><div id="comments-container-33042" class="comments-container"><span id="33058"></span><div id="comment-33058" class="comment"><div id="post-33058-score" class="comment-score"></div><div class="comment-text"><p>grahamb, much appreciated food for thought, BTW, your <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark link</a> also points to <a href="http://pcapdotnet.codeplex.com/">Pcap.Net</a>. FWIW, given that i may have to analyze more files in the future, my hope was to be able to automate the process; i've always dealt with WireShark files manually but that is really time consuming ... <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark link</a> looks like it is well worth some of my limited time to check out thoroughly.</p></div><div id="comment-33058-info" class="comment-info"><span class="comment-age">(25 May '14, 08:24)</span> <span class="comment-user userinfo">gerryLowry</span></div></div><span id="33059"></span><div id="comment-33059" class="comment"><div id="post-33059-score" class="comment-score"></div><div class="comment-text"><p><a href="http://ask.wireshark.org/questions/7894/tshark-batch-file">tshark batch file</a> looks useful for creating .csv that [i hope] would be relatively easy to analyze programmatically and thus eliminate my need for a c# API.</p></div><div id="comment-33059-info" class="comment-info"><span class="comment-age">(25 May '14, 08:41)</span> <span class="comment-user userinfo">gerryLowry</span></div></div><span id="33070"></span><div id="comment-33070" class="comment"><div id="post-33070-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-33070-info" class="comment-info"><span class="comment-age">(25 May '14, 12:04)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="33142"></span><div id="comment-33142" class="comment"><div id="post-33142-score" class="comment-score"></div><div class="comment-text"><p><span>@Kurt</span> ... FWIW, i will accept grahamb's answer when i'm certain it's correct as it most likely is ... at the moment, i'm hoping that someone may be aware of something that grahamb might not have yet discovered ... the challenge with programming is that there is so much to know and so little time ... i've been programming since 1967 and still feel that i'm mostly ignorant about what's available; Kurt, i do appreciate your hint ... far too many questions with answers do get orphaned.</p></div><div id="comment-33142-info" class="comment-info"><span class="comment-age">(28 May '14, 13:46)</span> <span class="comment-user userinfo">gerryLowry</span></div></div></div><div id="comment-tools-33042" class="comment-tools"></div><div class="clear"></div><div id="comment-33042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

