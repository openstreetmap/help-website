+++
type = "question"
title = "[closed] how to access data in such table?"
description = '''Hi, I&#x27;m writing a program with lua. I have data that organized in the following way: t= {i1{p1{,,,},p2{,,,},...pm{,,,}},i2{p1{,,,},p2{,,,},...pm{,,,}},...,in{p1{,,,},p2{,,,},...pm{,,,}}} (inner tables) In another way each group of data is indexed by two variables i&amp;amp;p,I am sure that the data is k...'''
date = "2012-02-17T19:24:00Z"
lastmod = "2012-02-25T17:08:00Z"
weight = 9111
keywords = [ "lua" ]
aliases = [ "/questions/9111" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] how to access data in such table?](/questions/9111/how-to-access-data-in-such-table)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9111-score" class="post-score" title="current number of votes">0</div><span id="post-9111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm writing a program with lua. I have data that organized in the following way: t= {i1{p1{,,,},p2{,,,},...pm{,,,}},i2{p1{,,,},p2{,,,},...pm{,,,}},...,in{p1{,,,},p2{,,,},...pm{,,,}}} (inner tables) In another way each group of data is indexed by two variables i&amp;p,I am sure that the data is kept correctly but I want a way to print the data from their tables because I won't know the values of i and p to iterate over them or even the numbers n &amp; m any body know how to do this with lua?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '12, 19:24</strong></p><img src="https://secure.gravatar.com/avatar/912ebc145cb38ec3da99be6003d7d9b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leena&#39;s gravatar image" /><p><span>Leena</span><br />
<span class="score" title="51 reputation points">51</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leena has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>25 Feb '12, 17:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-9111" class="comments-container"><span id="9113"></span><div id="comment-9113" class="comment"><div id="post-9113-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately off topic. You've asked a <em>general</em> Lua programming question as opposed to a <em>Wireshark</em> Lua question. Skilled Lua developers at <a href="http://stackoverflow.com">stackoverflow</a> are waiting to answer your question. :-)</p></div><div id="comment-9113-info" class="comment-info"><span class="comment-age">(17 Feb '12, 22:15)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="9114"></span><div id="comment-9114" class="comment"><div id="post-9114-score" class="comment-score"></div><div class="comment-text"><p>the program process data that coming from wireshark, the i is a source ip address and p is the port number and the data in the innermost table are destination ips</p></div><div id="comment-9114-info" class="comment-info"><span class="comment-age">(17 Feb '12, 22:31)</span> <span class="comment-user userinfo">Leena</span></div></div><span id="9115"></span><div id="comment-9115" class="comment"><div id="post-9115-score" class="comment-score"></div><div class="comment-text"><p>Ok, I see, but it's still off topic unless the data can only be printed with the help of Wireshark Lua, which isn't true in your case because the source IP is just a string, and the port number is just an integer. (Hint: you're looking to dump a Lua table...it's rather trivial to do...just Google it)</p></div><div id="comment-9115-info" class="comment-info"><span class="comment-age">(17 Feb '12, 22:45)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="9212"></span><div id="comment-9212" class="comment"><div id="post-9212-score" class="comment-score"></div><div class="comment-text"><p><a href="http://stackoverflow.com/questions/9339268/how-to-access-data-in-such-table">http://stackoverflow.com/questions/9339268/how-to-access-data-in-such-table</a></p></div><div id="comment-9212-info" class="comment-info"><span class="comment-age">(25 Feb '12, 17:08)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-9111" class="comment-tools"></div><div class="clear"></div><div id="comment-9111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "http://stackoverflow.com/questions/9339268/how-to-access-data-in-such-table" by helloworld 25 Feb '12, 17:07

</div>

</div>

</div>

