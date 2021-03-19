+++
type = "question"
title = "Last Login details for a Telnet session"
description = '''Using WireShark when I do a follow TCP stream on a Telnet packet it just gives a value like : Sat Nov 27 20:11:43 for the Last Login details. How can I get the year corresponding to this date for any telnet packet. Thanks Abhishek K'''
date = "2013-09-22T15:09:00Z"
lastmod = "2013-09-23T01:03:00Z"
weight = 25077
keywords = [ "telnet" ]
aliases = [ "/questions/25077" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Last Login details for a Telnet session](/questions/25077/last-login-details-for-a-telnet-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25077-score" class="post-score" title="current number of votes">0</div><span id="post-25077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using WireShark when I do a follow TCP stream on a Telnet packet it just gives a value like : Sat Nov 27 20:11:43 for the Last Login details. How can I get the year corresponding to this date for any telnet packet.</p><p>Thanks Abhishek K</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-telnet" rel="tag" title="see questions tagged &#39;telnet&#39;">telnet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '13, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/782001967c824c002a46c8c9bb4f6b39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MetalGeek7&#39;s gravatar image" /><p><span>MetalGeek7</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MetalGeek7 has no accepted answers">0%</span></p></div></div><div id="comments-container-25077" class="comments-container"></div><div id="comment-tools-25077" class="comment-tools"></div><div class="clear"></div><div id="comment-25077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25080"></span>

<div id="answer-container-25080" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25080-score" class="post-score" title="current number of votes">0</div><span id="post-25080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>when I do a follow TCP stream on a Telnet packet it just gives a value like : <strong>Sat Nov 27 20:11:43 for the Last Login details</strong></p></blockquote><p>Follow TCP stream collects the bytes transferred in a conversation, so the date you see is what the telnet server sent to the telnet client (obviously the date of the last login). Wireshark cannot reformat that date, as it's just some text sent in the telnet connection. <strong>If the server did not send the year (the message actually comes from the login process), there is nothing Wireshark can do about it.</strong> Most certainly it would be the current year. So, if you need the year, you could look at the time stamp of the packet. It's the second column in the GUI (Time). You can change the time format like this:</p><blockquote><p>View -&gt; Time Display Format -&gt; choose whatever you need</p></blockquote><p>However that will just reflect the date/time on the machine that captured the data at the time it did capture the data. That is not necessarily the 'real' date/time. If the date of the capture machine was off by several years, you wouldn't be able to detect that.</p><p>Let's say:</p><p>The telnet session took place at: <strong>2012</strong> Nov 27 20:11:43. Follow TCP stream shows only: <strong>Nov 27 20:11:43</strong><br />
The date/time on the capture machine was: <strong>2010</strong> Dec 05 15:11:00</p><p>So, if you now assume that the last login was at: <strong>2010 Nov 27 20:11:43</strong>, that <strong>would be (obviously) wrong</strong>.</p><blockquote><p>How can I get the year corresponding to this date <strong>for any telnet packet</strong>.</p></blockquote><p>Can you please add some information about this? I don't understand what you are asking for. It it's what I'm describing above, just ignore this question.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '13, 16:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Sep '13, 01:57</strong> </span></p></div></div><div id="comments-container-25080" class="comments-container"><span id="25084"></span><div id="comment-25084" class="comment"><div id="post-25084-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>What I meant was to just get the complete information about the last login for the telnet session. I saw while doing a follow TCP stream that the year information was missing in the last login attribute, so just wanted to know if there is any way by which I can get that.</p><p>Thanks</p></div><div id="comment-25084-info" class="comment-info"><span class="comment-age">(22 Sep '13, 17:37)</span> <span class="comment-user userinfo">MetalGeek7</span></div></div><span id="25099"></span><div id="comment-25099" class="comment"><div id="post-25099-score" class="comment-score"></div><div class="comment-text"><p>As I tried to explain: That is just a text string sent from the server to the client. As the year is not included, Wireshark cannot display it. So, there is nothing you can do about it, as the information about the year is simply not there (in the capture file).</p><p>The "problem" is the login process on the system where your logged in. Maybe you can change the behavior of that. See 'man login' on your Linux/Unix system.</p></div><div id="comment-25099-info" class="comment-info"><span class="comment-age">(23 Sep '13, 01:03)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-25080" class="comment-tools"></div><div class="clear"></div><div id="comment-25080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25098"></span>

<div id="answer-container-25098" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25098-score" class="post-score" title="current number of votes">0</div><span id="post-25098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Using WireShark when I do a follow TCP stream on a Telnet packet it just gives a value like : Sat Nov 27 20:11:43 for the Last Login details.</p></blockquote><p>That's because the operating system on the machine to which you telnetted printed out "Sat Nov 27 20:11:43" as the last login date when you logged in, without printing the year. That has nothing to do with Telnet, and everything to do with the program on that machine that implements the login process. If it's not printing the year of the last login, you would have to either:</p><ol><li>configure that program to print the year <em>if</em> that's possible;</li><li>modify it to print the year if you have source code to it, know enough to modify it, have the tools necessary to build your modified version, and have the privileges necessary to install the modified version;</li><li>find where it stores that information and, if what it stores is sufficient to get the year, see whether you can fetch the information from there (e.g. the <code>/var/log/lastlog</code> file on some UN*X systems).</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '13, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-25098" class="comments-container"></div><div id="comment-tools-25098" class="comment-tools"></div><div class="clear"></div><div id="comment-25098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

