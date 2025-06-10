+++
type = "question"
title = "The Rails Port is Very slow to open over public IP"
description = '''Hello,  I have setup my internal The Rails Port which runs on 3000, when i am trying to access it over public IP , example : http://lab.mydomain.co.uk:3000/ , this is horrible slow!!! , but internally its fine no issues at all ,  its not that my internet bandwidth is slow , so why its so slow ? is t...'''
date = "2018-06-10T22:05:00Z"
lastmod = "2018-06-11T00:41:00Z"
weight = 64148
keywords = [ "osm", "port", "rails" ]
aliases = [ "/questions/64148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [The Rails Port is Very slow to open over public IP](/questions/64148/the-rails-port-is-very-slow-to-open-over-public-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64148-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have setup my internal The Rails Port which runs on 3000, when i am trying to access it over public IP , example : <a href="http://lab.mydomain.co.uk:3000/">http://lab.mydomain.co.uk:3000/</a> , this is horrible slow!!! , but internally its fine no issues at all , its not that my internet bandwidth is slow , so why its so slow ?</p>
<p>is there any explanation like security handshake or some thing like this ?</p>
<p>Please help me her.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-rails" rel="tag" title="see questions tagged &#39;rails&#39;">rails</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jun '18, 22:05</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb2a94f867841b58214be09992831d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fosiul&#39;s gravatar image" />
<p><span>fosiul</span><br />
<span class="score" title="96 reputation points">96</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fosiul has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-64148" class="comments-container">
<span id="64150"></span>
<div id="comment-64150" class="comment">
<div id="post-64150-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you run something else on port 3000 and connect to that (a simple web server perhaps), is it still slow? It might be that your ISP is throttling traffic on port 3000.</p>
<p>If you'd like people to help you'll need to provide a bit more information - "horrible slow" doesn't describe what you've have done to try and investigate and resolve the problem. It's a bit like saying "my car won't go" without providing any more information (Does the engine turn over? Have some scallies nicked the wheels?).</p>
</div>
<div id="comment-64150-info" class="comment-info">
<span class="comment-age">(10 Jun '18, 23:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="64151"></span>
<div id="comment-64151" class="comment">
<div id="post-64151-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>, Thanks for the reply. I think i am understanding the probelem, its not with ISP, as we have dedicated businss line with unmanaed router.</p>
<p>i was testing with anoer link where i am using leaftlate with internal tiles , when i am calling this over public domain port 80, its actually unable to resolve the internal Ip when calling like this opaque: false, url: 'http://192.168.1.32/hot/{z}/{x}/{y}.png'</p>
<p>so had to chagne it to url: 'http://publicdomain.co.uk/hot/{z}/{x}/{y}.png' but then its slow ( i guess for DNS Query), so had to eidt host file to map manually domain with interal IP, now its fine.</p>
<p>let me try the same with Rails Port, i will come back tomorrow</p>
<p>Thanks for the help</p>
</div>
<div id="comment-64151-info" class="comment-info">
<span class="comment-age">(11 Jun '18, 00:41)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
</div>
<div id="comment-tools-64148" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64148-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

