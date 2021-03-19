+++
type = "question"
title = "Using wireshark to control a website&#x27;s AJAX"
description = '''I asked this question on stackoverflow and was told &quot;Use Wireshark&quot;. I&#x27;m a noob, and see nothing on your site I recognize as related to my question. I&#x27;m using perl to scrape data from a website. Now the website has changed, so it only loads the data via AJAX in response to entry into a textbox and c...'''
date = "2014-03-16T00:32:00Z"
lastmod = "2014-03-16T07:10:00Z"
weight = 30851
keywords = [ "ajax", "perl" ]
aliases = [ "/questions/30851" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Using wireshark to control a website's AJAX](/questions/30851/using-wireshark-to-control-a-websites-ajax)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30851-score" class="post-score" title="current number of votes">0</div><span id="post-30851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I asked this question on stackoverflow and was told "Use Wireshark". I'm a noob, and see nothing on your site I recognize as related to my question.</p><p>I'm using perl to scrape data from a website. Now the website has changed, so it only loads the data via AJAX in response to entry into a textbox and clicking a submit button.</p><p>How can my perl program simulate that user input and capture the resulting new page?</p><p>Is this something that Wireshark can help me with?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ajax" rel="tag" title="see questions tagged &#39;ajax&#39;">ajax</span> <span class="post-tag tag-link-perl" rel="tag" title="see questions tagged &#39;perl&#39;">perl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '14, 00:32</strong></p><img src="https://secure.gravatar.com/avatar/d0d62c9f798697f2c32f86d66f5e4a86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hsfrey&#39;s gravatar image" /><p><span>hsfrey</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hsfrey has no accepted answers">0%</span></p></div></div><div id="comments-container-30851" class="comments-container"></div><div id="comment-tools-30851" class="comment-tools"></div><div class="clear"></div><div id="comment-30851-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="30853"></span>

<div id="answer-container-30853" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30853-score" class="post-score" title="current number of votes">0</div><span id="post-30853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The guys at StackOverflow probably meant that you could use Wireshark to capture the traffic of a normal website visit (via manually browsing to it), and than capture what your perl script does and compare the requests and answer content. At least that's what I would do to make sure my script mimics the manual way of accessing the site.</p><p>Very often a site not only looks at the URL that you pass in the request, but also the referrer, user agent, cookies and other details carried in the HTTP header of the request. So Wireshark can show you what they are when surfing on the site with a browser. Use these values and mimic them in your script, and it should work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '14, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-30853" class="comments-container"></div><div id="comment-tools-30853" class="comment-tools"></div><div class="clear"></div><div id="comment-30853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30856"></span>

<div id="answer-container-30856" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30856-score" class="post-score" title="current number of votes">0</div><span id="post-30856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I recognize as related to my question.</p></blockquote><p>well, <strong>what</strong> was you question on stackoverflow !?!</p><blockquote><p>How can my perl program simulate that user input and capture the resulting new page?</p></blockquote><p>how did you figure out the structure of the web site in the first place? Just repeat that step for the new site structure</p><blockquote><p>Is this something that Wireshark can help me with?</p></blockquote><p>It will show you requests and responses to/from the site. However, in your case any browser developer tool (like Firebug for Firefox) would be much better.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '14, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Mar '14, 13:15</strong> </span></p></div></div><div id="comments-container-30856" class="comments-container"></div><div id="comment-tools-30856" class="comment-tools"></div><div class="clear"></div><div id="comment-30856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30859"></span>

<div id="answer-container-30859" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30859-score" class="post-score" title="current number of votes">0</div><span id="post-30859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might also want to take a look at an intercepting web proxy like Burpsuite (<a href="http://portswigger.net/burp/).">http://portswigger.net/burp/).</a> You can intercept and examine the packets flowing in each direction in real time, and use that information to make adjustments in your perl script. The free version of Burpsuite should be sufficient for the task.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '14, 07:10</strong></p><img src="https://secure.gravatar.com/avatar/b260fb38b621169269b5030f1ed6b766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="griff&#39;s gravatar image" /><p><span>griff</span><br />
<span class="score" title="361 reputation points">361</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="griff has 2 accepted answers">10%</span></p></div></div><div id="comments-container-30859" class="comments-container"></div><div id="comment-tools-30859" class="comment-tools"></div><div class="clear"></div><div id="comment-30859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

