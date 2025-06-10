+++
type = "question"
title = "API - Read Only with Basic Authentication?"
description = '''Hi, When making calls to http://api.openstreetmap.org/api/0.6/ to update elements I am getting a &quot;405 (Method not allowed)&quot; response. I could swear it was working a week or so ago... The Basic Authentication itself seems to be working - if I use a dummy user name and/or password I get a 401 Unauthor...'''
date = "2017-04-13T20:17:00Z"
lastmod = "2017-04-14T22:46:00Z"
weight = 55590
keywords = [ "development", "basic_authentication", "http_status_code_405", "api", "https" ]
aliases = [ "/questions/55590" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [API - Read Only with Basic Authentication?](/questions/55590/api-read-only-with-basic-authentication)

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
<span id="post-55590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55590-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, When making calls to <a href="http://api.openstreetmap.org/api/0.6/">http://api.openstreetmap.org/api/0.6/</a> to update elements I am getting a "405 (Method not allowed)" response. I could swear it was working a week or so ago...</p>
<p>The Basic Authentication itself seems to be working - if I use a dummy user name and/or password I get a 401 Unauthorized. With the same authentication I can get the permissions using /api/0.6/permissions and they are all there. But when I go to do an actual update (opening and closing the changeset is working fine) I get the "405 (Method not allowed)". I am using PUT (as per the documentation) but I have tried using POST - same results. The response includes this header: "Allow: GET, HEAD, OPTIONS".</p>
<p>Using https instead of http gives the same result, so I am sticking with http for the moment for ease of debugging (with Wireshark.)</p>
<p>Using the same account with Potlatch has no problems - but that uses OAuth instead of Basic Auth.</p>
<p>Am I doing something wrong? Has updating via Basic Auth been turned off deliberately? Any ideas?</p>
<hr />
<p>A bit background - this is how I issue requests to the server:</p>
<pre><code>I am working in VB.Net using HttpWebRequest
Typical url is http://api.openstreetmap.org/api/0.6/relation/12345, using PUT, with XML payload
Basic Authentication being added like this:
                Dim cre As String = $&quot;{Credentials.UserName}:{Credentials.Password}&quot;
                Dim bytes As Byte() = System.Text.Encoding.ASCII.GetBytes(cre)
                Dim base64 As String = Convert.ToBase64String(bytes)
                req.Headers.Add(“Authorization”, “Basic ” + base64)
Payload written like this:
                Dim b() As Byte
                b = System.Text.Encoding.UTF8.GetBytes(sPayload)
                req.ContentLength = b.Length
                req.ContentType = &quot;application/xml; charset=utf-8&quot;
                With req.GetRequestStream
                    .Write(b, 0, b.Length)
                    .Close()
                End With</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-basic_authentication" rel="tag" title="see questions tagged &#39;basic_authentication&#39;">basic_authentication</span> <span class="post-tag tag-link-http_status_code_405" rel="tag" title="see questions tagged &#39;http_status_code_405&#39;">http_status_code_405</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Apr '17, 20:17</strong></p>
<img src="https://secure.gravatar.com/avatar/81868786ff539d9a5b1f21ed57b6e13a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="csmale&#39;s gravatar image" />
<p><span>csmale</span><br />
<span class="score" title="81 reputation points">81</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="csmale has one accepted answer">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '18, 23:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-55590" class="comments-container">
<span id="55591"></span>
<div id="comment-55591" class="comment">
<div id="post-55591-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>not sure if that is related: but could you mention how you are issuing the requests to the server?</p>
<p>Thanks for the additional info, I have merge it to your question text.</p>
</div>
<div id="comment-55591-info" class="comment-info">
<span class="comment-age">(13 Apr '17, 20:45)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="55596"></span>
<div id="comment-55596" class="comment">
<div id="post-55596-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>For testing please use the development API, see <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#URL_.2B_authentication">https://wiki.openstreetmap.org/wiki/API_v0.6#URL_.2B_authentication</a> .</p>
</div>
<div id="comment-55596-info" class="comment-info">
<span class="comment-age">(13 Apr '17, 21:18)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="55601"></span>
<div id="comment-55601" class="comment">
<div id="post-55601-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I currently get an error message when I try to upload from JOSM: Communication with the JOSM server 'https://api.openstreetmap.org/api/0.6/' timed out. ... However, I am using OAuth and Test Access Token works fine. Could it be that there is a general issue with uploads via this API?</p>
</div>
<div id="comment-55601-info" class="comment-info">
<span class="comment-age">(13 Apr '17, 23:19)</span> <span class="comment-user userinfo">Nachtspazz</span>
</div>
</div>
<span id="55602"></span>
<div id="comment-55602" class="comment">
<div id="post-55602-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Before you do -anything- more: DO NOT TEST AGAINST THE PRODUCTION API</p>
<p>Use one of the dev API and create objects there with the iD instance that runs on them. Further if you a planning to do a mechanical edit you need to think about following the corresponding guideline: <a href="http://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct">http://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct</a></p>
</div>
<div id="comment-55602-info" class="comment-info">
<span class="comment-age">(13 Apr '17, 23:46)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="55603"></span>
<div id="comment-55603" class="comment">
<div id="post-55603-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have created an object in the test DB which is good enough for testing for now.</p>
<p>Testing on the dev instance shows different results. Despite my credentials being correct, attempting to create a changeset is giving "401 Unauthorized" (yes I know the dev credentials are separate from prod). A request to <a href="http://api06">http://api06</a> redirects to http<strong>s</strong>://master so I can't see what happens on the wire at the moment.</p>
<p>I can see two possible ways forward. Debugging the https stream with Fiddler, or giving up on Basic Authentication and implementing OAuth. Personally I will be happy with Basic over https, and OAuth looks like being quite a bit of work. When the authentication works again, I could also rewrite the code to use osmChange uploads instead of the regular update API, if I can't get the update API to accept a PUT or a POST.</p>
<p>Has anyone got some example code or an example application for a simple update (not an osmChange upload) with Basic Auth that is <em>working today</em>?</p>
</div>
<div id="comment-55603-info" class="comment-info">
<span class="comment-age">(14 Apr '17, 07:45)</span> <span class="comment-user userinfo">csmale</span>
</div>
</div>
<span id="55605"></span>
<div id="comment-55605" class="comment not_top_scorer">
<div id="post-55605-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By the way, my use case is nothing dramatic, just saving me a bit of typing - small numbers of individual updates to existing objects, each individually reviewed by me. It is neither bulk, nor blind. So I am assuming that it does not fall under the scope of the Automated Edits CoC which refers to "other systematic edits to the database by other means without consideration of each change."</p>
</div>
<div id="comment-55605-info" class="comment-info">
<span class="comment-age">(14 Apr '17, 07:46)</span> <span class="comment-user userinfo">csmale</span>
</div>
</div>
</div>
<div id="comment-tools-55590" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-55590-form-container" class="comment-form-container">
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

<span id="55613"></span>

<div id="answer-container-55613" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55613-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aseerel4c26 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Found the problem, thanks to Fiddler.... For debugging I was using http URLs. The server was returning a 301 permanent redirect to an https URL, which HttpWebRequest was handling automatically, resending the original request to the new location. However, the Authentication header is deliberately stripped when it follows the redirect, which makes sense when you think about it. Net result is that all the requests were unauthenticated.</p>
<p>So it works if I avoid the redirects by using the ultimate URL (<a href="https://master">https://master</a>....) in the original request.</p>
<p>So now I have to turn off automatic redirect handling and handle it myself, but that looks pretty simple (famous last words...)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '17, 20:42</strong></p>
<img src="https://secure.gravatar.com/avatar/81868786ff539d9a5b1f21ed57b6e13a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="csmale&#39;s gravatar image" />
<p><span>csmale</span><br />
<span class="score" title="81 reputation points">81</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="csmale has one accepted answer">16%</span></p>
</div>
</div>
<div id="comments-container-55613" class="comments-container">
<span id="55614"></span>
<div id="comment-55614" class="comment">
<div id="post-55614-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta: thanks, so this question is solved now?</p>
</div>
<div id="comment-55614-info" class="comment-info">
<span class="comment-age">(14 Apr '17, 22:00)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="55615"></span>
<div id="comment-55615" class="comment">
<div id="post-55615-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, the question is answered for me... Sorry, is there some button I have to push to mark this question as "answered"? I am not familiar with this board, it doesn't seem to work quite the same as other forums.</p>
</div>
<div id="comment-55615-info" class="comment-info">
<span class="comment-age">(14 Apr '17, 22:39)</span> <span class="comment-user userinfo">csmale</span>
</div>
</div>
<span id="55616"></span>
<div id="comment-55616" class="comment">
<div id="post-55616-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11526/csmale"></a><a href="https://help.openstreetmap.org/users/11526/csmale">@csmale</a>: don't worry. There is the <a href="/questions/34318/how-to-mark-an-answer-as-accepted-and-mark-my-question-as-answered">"accepted"</a> button, however, that does not work for self-answered questions. I did for you now.</p>
</div>
<div id="comment-55616-info" class="comment-info">
<span class="comment-age">(14 Apr '17, 22:46)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55613-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55595"></span>

<div id="answer-container-55595" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55595-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Basic Authentication should still work (e.g. <a href="https://josm.openstreetmap.de/wiki/Help/Preferences/Connection#Basicauthentication">JOSM supports it</a>).</p>
<p>Just a vague guess: try to supply a meaningful user agent with the HTTP request. I guess you are currently using nothing or "VB.net".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '17, 21:18</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-55595" class="comments-container">
<span id="55598"></span>
<div id="comment-55598" class="comment">
<div id="post-55598-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the comments so far...</p>
<p>I have looked at JOSMs traffic with Wireshark - after setting JOSM to use Basic Auth with http. It does indeed work, but it uses a different call - POST on &lt;changeset&gt;/upload with an osmChange payload whereas I am using a PUT with an osm payload. What I am doing is according to the API documentation as far as I can see...</p>
<p>I tried to use the dev API but the database is empty so I would have to actually write code to create an object first. All I am actually trying to do is to update a single tag.</p>
<p>Is the user agent seriously relevant here? Does the API behaviour change according to the user agent string?</p>
</div>
<div id="comment-55598-info" class="comment-info">
<span class="comment-age">(13 Apr '17, 21:30)</span> <span class="comment-user userinfo">csmale</span>
</div>
</div>
<span id="55600"></span>
<div id="comment-55600" class="comment">
<div id="post-55600-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11526/csmale"></a><a href="https://help.openstreetmap.org/users/11526/csmale">@csmale</a>: as said, the agent thing was just a guess. I do not know if there is possibly some blocking in place. Also it would not explain the 405 HTTP response. Let's wait a bit until someone more knowingly comes by.</p>
<p>Regarding the dev database: just add objects using JOSM.</p>
</div>
<div id="comment-55600-info" class="comment-info">
<span class="comment-age">(13 Apr '17, 21:42)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55595" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55595-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

