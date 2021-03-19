+++
type = "question"
title = "Extract to Csv selected data"
description = '''Hi  I&#x27;d like to extract selected data in the packet details. Payload length, duration and bits. How can I do this? I see payload length and bits in the packet details, but duration in statistics-conversations.  How can I get these data from a capture to a CSV?  Here&#x27;s the image migrated from the com...'''
date = "2016-09-08T12:04:00Z"
lastmod = "2016-09-12T22:10:00Z"
weight = 55401
keywords = [ "csv" ]
aliases = [ "/questions/55401" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract to Csv selected data](/questions/55401/extract-to-csv-selected-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55401-score" class="post-score" title="current number of votes">0</div><span id="post-55401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I'd like to extract selected data in the packet details. Payload length, duration and bits. How can I do this? I see payload length and bits in the packet details, but duration in statistics-conversations.</p><p>How can I get these data from a capture to a CSV?</p><p>Here's the image migrated from the comment below: <img src="https://osqa-ask.wireshark.org/upfiles/conversation_4q3VO0a.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '16, 12:04</strong></p><img src="https://secure.gravatar.com/avatar/dce851b25638fdbabdfc55a27f8dbb6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rsharkz&#39;s gravatar image" /><p><span>Rsharkz</span><br />
<span class="score" title="5 reputation points">5</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rsharkz has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Sep '16, 22:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-55401" class="comments-container"></div><div id="comment-tools-55401" class="comment-tools"></div><div class="clear"></div><div id="comment-55401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55402"></span>

<div id="answer-container-55402" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55402-score" class="post-score" title="current number of votes">0</div><span id="post-55402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to avoid (or at least minimize) any post-processing, you can use tshark with <code>-T fields -e field1 -e field2 -e field3 -E separator=,</code> command line parameters to get a file with a line <code>field1,field2,field3</code> representing each frame in the capture (see <a href="https://www.wireshark.org/docs/man-pages/tshark.html">the tshark manual page</a> for details about separators and handling of multiple instances of the same field in a single frame, as you need to configure also an instance separator if you decide to print all of them). But what exactly do you mean by the "duration" you can get in statistics in the context of a csv file with one line per frame?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '16, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55402" class="comments-container"><span id="55405"></span><div id="comment-55405" class="comment"><div id="post-55405-score" class="comment-score"></div><div class="comment-text"><p>Hi sindy,</p><p>thanks for your answer. I have attached an image showing the field that i want. It is called Duration (I circled the field in red in the image). To get the duration, i clicked on statistics, and then conversations. My tshark is not coming up (im using windows 8.1). any idea why?</p><p>The image is in the question.</p></div><div id="comment-55405-info" class="comment-info"><span class="comment-age">(08 Sep '16, 17:13)</span> <span class="comment-user userinfo">Rsharkz</span></div></div><span id="55410"></span><div id="comment-55410" class="comment"><div id="post-55410-score" class="comment-score"></div><div class="comment-text"><p><span>@Rsharkz</span>,</p><p>a housekeeping note: an Answer must answer the original Question, hence I've converted your post into a Comment. To do that, I had to migrate the picture to the Question, as pictures in Comments kill page layouts.</p><p>To the subject: I did suspect that you had in mind the duration of a conversation, but I better asked because it was (and still is) not clear to me how you'd want to combine columns from the statistics view (one line per conversation which may contain multiple frames) with columns from frame dissection (one line per frame which makes just a part of a conversation).</p><p>Do you want the lines of the resulting csv to represent the individual frames but have the "conversation duration" column at each of the lines which gives the duration of the conversation to which that line's source frame belongs?</p></div><div id="comment-55410-info" class="comment-info"><span class="comment-age">(08 Sep '16, 22:18)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="55413"></span><div id="comment-55413" class="comment"><div id="post-55413-score" class="comment-score"></div><div class="comment-text"><p><span>@sindy</span></p><p>Thanks and noted the house rules, apologies as I just started in the forum :)</p><p>Yes, I want the lines of the resulting csv to have a line per frame, which includes the duration of the conversation.</p><p>Is the duration of conversation per frame the total amount of time a packet completes its communication. Ideally, I would like to monitor how long each packet takes to complete the entire session.</p><p>The statistics inside tshark - can we create custom fields to perform a subtraction or an addition or average? For example, I'd like to find out the average no of packets or packet length received every minute. I probably can run something off the CSV, but just want to find out if tshark has an option for that.</p></div><div id="comment-55413-info" class="comment-info"><span class="comment-age">(08 Sep '16, 23:36)</span> <span class="comment-user userinfo">Rsharkz</span></div></div><span id="55414"></span><div id="comment-55414" class="comment"><div id="post-55414-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Is the duration of conversation per frame the total amount of time a packet completes its communication.</p></blockquote><p>Please reword this sentence - it looks to me as if something is missing in it.</p><blockquote><p>Ideally, I would like to monitor how long each packet takes to complete the entire session.</p></blockquote><p>Same case. I admit I'm not a native English speaker so I may miss some grammar constructions.</p></div><div id="comment-55414-info" class="comment-info"><span class="comment-age">(08 Sep '16, 23:47)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="55505"></span><div id="comment-55505" class="comment"><div id="post-55505-score" class="comment-score"></div><div class="comment-text"><p>hi sindy. How do I use tshark to extract the duration column in the screenshot (the image you moved to the question)?</p><p>That's what I would like to do. Thanks!</p></div><div id="comment-55505-info" class="comment-info"><span class="comment-age">(12 Sep '16, 20:18)</span> <span class="comment-user userinfo">Rsharkz</span></div></div><span id="55508"></span><div id="comment-55508" class="comment not_top_scorer"><div id="post-55508-score" class="comment-score"></div><div class="comment-text"><p>The closest possibility to what you want is</p><p><code>tshark -r your_input_file_name -Q -z conv,tcp &gt; your_output_file_name.csv</code></p><p>except that the output is not a literal csv - the values in the output table are not separated by commas but by spaces and, occasionally, some additional formatting character sequences like <code>&lt;-&gt;</code>, so you'll have to do a bit of text processing.</p></div><div id="comment-55508-info" class="comment-info"><span class="comment-age">(12 Sep '16, 22:10)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-55402" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-55402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

