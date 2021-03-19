+++
type = "question"
title = "Understanding IP packet flow during a login process"
description = '''When analyzing a capture of a login, how do you determine how many IP packets were generated during the process of the login? I guess part of the answer would need to address how to determine which packets were part of the process so the question is probably better worded as: how are IP packets iden...'''
date = "2013-11-21T22:13:00Z"
lastmod = "2013-11-22T02:12:00Z"
weight = 27251
keywords = [ "count", "ip", "login", "packets" ]
aliases = [ "/questions/27251" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Understanding IP packet flow during a login process](/questions/27251/understanding-ip-packet-flow-during-a-login-process)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27251-score" class="post-score" title="current number of votes">0</div><span id="post-27251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When analyzing a capture of a login, how do you determine how many IP packets were generated during the process of the login? I guess part of the answer would need to address how to determine which packets were part of the process so the question is probably better worded as: how are IP packets identified as part of the login?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-count" rel="tag" title="see questions tagged &#39;count&#39;">count</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-login" rel="tag" title="see questions tagged &#39;login&#39;">login</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '13, 22:13</strong></p><img src="https://secure.gravatar.com/avatar/9af5211d364be21653583ede387ca87b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pj88&#39;s gravatar image" /><p><span>pj88</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pj88 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Nov '13, 03:02</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-27251" class="comments-container"></div><div id="comment-tools-27251" class="comment-tools"></div><div class="clear"></div><div id="comment-27251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27255"></span>

<div id="answer-container-27255" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27255-score" class="post-score" title="current number of votes">2</div><span id="post-27255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>IP doesn't really care about logins. That kind of information is exchanged on much higher layers, e.g. HTTP or FTP etc. So you need to ask yourself a different question: How does the login process work? What protocol does it use? And how many packets do you need to exchange the information for that?</p><p>Logins can work quite differently for different protocols: some just send a packet saying "this is my username, this is my password, and I'd like to login". Others do it in a much more complex way:</p><ol><li>Client: "Hello, I'd like to login."</li><li>Server: "Great. Send me your username"</li><li>Client "Username is abc"</li><li>Server. "Nice. Now the password for abc please"</li><li>Client: "Password is def"</li><li>Server: "Works for me. Continue"</li></ol><p>That example needs at least 6 Packets, going back and forth, plus probably some for the TCP session setup. It can get even more complex, when there are Challenge-Response or Private/Public key mechanisms involved.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '13, 22:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Nov '13, 22:55</strong> </span></p></div></div><div id="comments-container-27255" class="comments-container"></div><div id="comment-tools-27255" class="comment-tools"></div><div class="clear"></div><div id="comment-27255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27264"></span>

<div id="answer-container-27264" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27264-score" class="post-score" title="current number of votes">1</div><span id="post-27264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>how are IP packets identified as part of the login?</p></blockquote><p>I would do it this way</p><ol><li>understand the login process for your application (as <span><span>@Jasper</span></span> explained)</li><li>right click a frame and select "Follow TCP stream"</li><li>In the pop-up windows find the <strong>first</strong> string that looks like being part of the login process, based on your definition.</li><li>Copy that string</li><li>Search that string in the packet list. Either CTRL-F or <code>frame contains "string"</code></li><li>From there, either look at each packet payload until you find the end of the login process or search again for a string that marks the end of the process (like a status code or so)</li><li>Count the number of frames between start and end.</li></ol><p>This will only work if the communication is <strong>not encrypted</strong> or you are <strong>able to decrypt</strong> it (SSL/TLS decryption in Wireshark).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '13, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Nov '13, 11:41</strong> </span></p></div></div><div id="comments-container-27264" class="comments-container"></div><div id="comment-tools-27264" class="comment-tools"></div><div class="clear"></div><div id="comment-27264-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

