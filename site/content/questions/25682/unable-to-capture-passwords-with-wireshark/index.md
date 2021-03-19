+++
type = "question"
title = "Unable to capture passwords with wireshark?"
description = '''To test the capturing of plain text, I have logged into my router (http://192.168.0.1) and given username and password applying http.request.method == &quot;POST&quot; filter. I have clicked on the captured packets and then expand the Hypertext Transfer Protocol field. The POST data were there, but i cant abl...'''
date = "2013-10-06T17:26:00Z"
lastmod = "2014-09-16T05:32:00Z"
weight = 25682
keywords = [ "router" ]
aliases = [ "/questions/25682" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to capture passwords with wireshark?](/questions/25682/unable-to-capture-passwords-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25682-score" class="post-score" title="current number of votes">0</div><span id="post-25682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>To test the capturing of plain text, I have logged into my router (<a href="http://192.168.0.1">http://192.168.0.1</a>) and given username and password applying <strong>http.request.method == "POST"</strong> filter. I have clicked on the captured packets and then expand the Hypertext Transfer Protocol field. The POST data were there, but i cant able to see username and passwords there.. Any help would be really helpful. Thank You.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '13, 17:26</strong></p><img src="https://secure.gravatar.com/avatar/b41802fe7f333c0b2b2b68be7da4f757?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karthick&#39;s gravatar image" /><p><span>Karthick</span><br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karthick has no accepted answers">0%</span></p></div></div><div id="comments-container-25682" class="comments-container"></div><div id="comment-tools-25682" class="comment-tools"></div><div class="clear"></div><div id="comment-25682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="25699"></span>

<div id="answer-container-25699" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25699-score" class="post-score" title="current number of votes">2</div><span id="post-25699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try using the popup menu of the connection that should have the password and select "Follow TCP stream". If you can't spot the password in there the connection is probably encrypted (or it is the wrong connection you selected).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '13, 00:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-25699" class="comments-container"></div><div id="comment-tools-25699" class="comment-tools"></div><div class="clear"></div><div id="comment-25699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25714"></span>

<div id="answer-container-25714" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25714-score" class="post-score" title="current number of votes">0</div><span id="post-25714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you search the password by using filters?</p><blockquote><p>frame contains abc123</p></blockquote><p>where abc123 is your password.</p><p>If there are no matches, the password is not sent in clear. In that case there is (most certainly) some javascript in use that scrambles the password for the POST request. If so, you'll have to analyze the script code or use a javascript debugger (google for Firefox developer tools).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '13, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-25714" class="comments-container"></div><div id="comment-tools-25714" class="comment-tools"></div><div class="clear"></div><div id="comment-25714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30458"></span>

<div id="answer-container-30458" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30458-score" class="post-score" title="current number of votes">0</div><span id="post-30458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>please, 1-&gt; right click on the "packet" to be captured 2-&gt; click on "Follow TCP Stream" 3-&gt; there you will find a line (in a new popup window) 4-&gt; the username will be shown on 2nd/3rd last line(of red-color text) 5-&gt; next to your username, a password would be shown(either in real-password or in encrypted/changed form)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '14, 21:29</strong></p><img src="https://secure.gravatar.com/avatar/92dc29c2384d725442c6a75c6764a029?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Asif%20Mehmood&#39;s gravatar image" /><p><span>Asif Mehmood</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Asif Mehmood has no accepted answers">0%</span></p></div></div><div id="comments-container-30458" class="comments-container"></div><div id="comment-tools-30458" class="comment-tools"></div><div class="clear"></div><div id="comment-30458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36362"></span>

<div id="answer-container-36362" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36362-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36362-score" class="post-score" title="current number of votes">0</div><span id="post-36362-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Use http.request.method == "GET"</li><li>then right click follow tcp stream</li><li>then switch the connection to "your ip --&gt; router ip"</li><li>find [Authentication : basic lkjsdhsjvsdugvsvjbn]</li><li>the above hash is base64 you can crack it if you are good at cryptography</li><li>otherwise there are some websites which will crack it for you, just paste the above hash (scrambled text) and voila !!!!!.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '14, 05:27</strong></p><img src="https://secure.gravatar.com/avatar/8bcf89b717dea15c0cec88562b6e7cb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mayhem&#39;s gravatar image" /><p><span>mayhem</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mayhem has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Sep '14, 05:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-36362" class="comments-container"><span id="36364"></span><div id="comment-36364" class="comment"><div id="post-36364-score" class="comment-score">1</div><div class="comment-text"><p>Hint for 5.: no need to be good at cryptography - base64 may be considered "obfuscation" at best. Decoding it is child's play.</p></div><div id="comment-36364-info" class="comment-info"><span class="comment-age">(16 Sep '14, 05:32)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-36362" class="comment-tools"></div><div class="clear"></div><div id="comment-36362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

