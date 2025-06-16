+++
type = "question"
title = "osm api 0.6 upload GPX track"
description = '''Hello guys, I quite fighting with OSM API v0.6 and upload GPX track task. I&#x27;m developing application for Android and trying to use this method. Firstly I though it should be a problem of login, so I changed login mechanism to OAuth. Anyway same result now. After selecting track and settings all para...'''
date = "2012-08-16T14:57:00Z"
lastmod = "2014-10-27T13:56:00Z"
weight = 15147
keywords = [ "api", "gpx", "upload", "locus" ]
aliases = [ "/questions/15147" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osm api 0.6 upload GPX track](/questions/15147/osm-api-06-upload-gpx-track)

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
<span id="post-15147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15147-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello guys,</p>
<p>I quite fighting with OSM API v0.6 and upload GPX track task. I'm developing application for Android and trying to use <a href="https://wiki.openstreetmap.org/wiki/Api06#Uploading_Traces">this</a> method. Firstly I though it should be a problem of login, so I changed login mechanism to OAuth. Anyway same result now.</p>
<p>After selecting track and settings all parameters (description ('test'), tags ('test'), visibility ('public')), uploading always return <strong>400 Bad Request</strong>, no content, no error message</p>
<pre><code>---------- REQUEST -----------
org.apache.http.client.methods.HttpPost@427e06f8, url: http://api.openstreetmap.org/api/0.6/gpx/create
headers: Content-Type: multipart/form-data
headers: Accept-Charset: ISO-8859-2, utf-8
headers: Accept-Encoding: gzip,deflate
headers: User-Agent: Locus/2.5.6 (Linux; U; Android; en-us)
HttpPost entity:com.google.android.common.http.MultipartEntity@427e0d98
&#10;---------- RESPONSE -----------
statusLine:HTTP/1.1 400 Bad Request
headers:Date, Thu, 16 Aug 2012 13:34:33 GMT
headers:Server, Apache/2.2.22 (Ubuntu)
headers:X-Powered-By, Phusion Passenger (mod_rails/mod_rack) 3.0.14
headers:Vary, Accept-Language,Accept-Encoding
headers:Content-Language, en
headers:Cache-Control, no-cache
headers:X-Request-Id, 0bbf0e2fd3e78e4f855718f7e53dbef5
headers:X-Runtime, 0.366059
headers:X-UA-Compatible, IE=Edge,chrome=1
headers:Status, 400
headers:Content-Encoding, gzip
headers:Content-Length, 21
headers:Connection, close
headers:Content-Type, text/html; charset=utf-8</code></pre>
<p>exactly same track uploaded by web site works. Have someone any idea or any method how to test what is problem on OSM server? Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span> <span class="post-tag tag-link-locus" rel="tag" title="see questions tagged &#39;locus&#39;">locus</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '12, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/d2aebf074a0667a95d09bf5c48baa12e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="menion&#39;s gravatar image" />
<p><span>menion</span><br />
<span class="score" title="88 reputation points">88</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="menion has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15147" class="comments-container">
<span id="15148"></span>
<div id="comment-15148" class="comment">
<div id="post-15148-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You should not use api.osm.org for testing and development. There is an instance of the api on a different database for that at api06.dev.openstreetmap.org</p>
</div>
<div id="comment-15148-info" class="comment-info">
<span class="comment-age">(16 Aug '12, 15:12)</span> <span class="comment-user userinfo">Gnonthgol ♦</span>
</div>
</div>
<span id="15151"></span>
<div id="comment-15151" class="comment">
<div id="post-15151-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I know. I was testing upload on api06.dev ... but it also not worked. So I tried direct upload by web site also on this api06.dev... where it also not work!! compare to normal api.open ... where upload of same file works without problem (upload deleted, don't worry)</p>
<p>anyway same result on both sites</p>
</div>
<div id="comment-15151-info" class="comment-info">
<span class="comment-age">(16 Aug '12, 15:29)</span> <span class="comment-user userinfo">menion</span>
</div>
</div>
</div>
<div id="comment-tools-15147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15147-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15171"></span>

<div id="answer-container-15171" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15171-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>after another fight-time, problem fixed - so just if anyone have same problem:</p>
<p>seems like OSM server cannot correctly handle <strong>com.google.android.common.http.MultipartEntity</strong> object. Solution is to use Apache <a href="http://hc.apache.org/downloads.cgi">HttpComponents</a> library and it's own implementation of <strong>MultipartEntity</strong> object. With this is no problem with posting GPX tracks</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '12, 20:41</strong></p>
<img src="https://secure.gravatar.com/avatar/d2aebf074a0667a95d09bf5c48baa12e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="menion&#39;s gravatar image" />
<p><span>menion</span><br />
<span class="score" title="88 reputation points">88</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="menion has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15171" class="comments-container">
<span id="37924"></span>
<div id="comment-37924" class="comment">
<div id="post-37924-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey, i am facing a similar problem with C# could you please explain your solution in detail.</p>
<p>Regards</p>
</div>
<div id="comment-37924-info" class="comment-info">
<span class="comment-age">(24 Oct '14, 14:03)</span> <span class="comment-user userinfo">Osm_Enthu</span>
</div>
</div>
<span id="37925"></span>
<div id="comment-37925" class="comment">
<div id="post-37925-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hello Enthu,</p>
<p>I'm worried, I can't help here more. Exact reason, why one solution work and second don't is not known to me. My solution was simply - I've changed library I used for different kind. So I can only suggest this to you. If you use any library for sending MutliPart objects over HTTP, then try different library.</p>
</div>
<div id="comment-37925-info" class="comment-info">
<span class="comment-age">(24 Oct '14, 14:25)</span> <span class="comment-user userinfo">menion</span>
</div>
</div>
</div>
<div id="comment-tools-15171" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15171-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38002"></span>

<div id="answer-container-38002" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38002-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thats for all of those who came stumbling here</p>
<p><a href="http://www.briangrinstead.com/blog/multipart-form-post-in-c">http://www.briangrinstead.com/blog/multipart-form-post-in-c</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '14, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/0be8b0bc55610645ad634cb9f680c48f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Osm_Enthu&#39;s gravatar image" />
<p><span>Osm_Enthu</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Osm_Enthu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38002" class="comments-container">
&#10;</div>
<div id="comment-tools-38002" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38002-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

