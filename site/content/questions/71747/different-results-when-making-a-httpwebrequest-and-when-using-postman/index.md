+++
type = "question"
title = "Different results when making a HttpWebRequest and when using Postman"
description = '''Hello, I am trying to get Geo coordinates from a .NET Web App using HttpWebRequest and requesting this link: https://nominatim.openstreetmap.org/search?q=2+$+2A+Cyclone+Street+3995+WONTHAGGI&amp;amp;country=au&amp;amp;format=json&amp;amp;addressdetails=1. In my app, I receive 10 results but none of them are fro...'''
date = "2019-11-20T11:56:00Z"
lastmod = "2019-12-02T11:11:00Z"
weight = 71747
keywords = [ "postman", "httpwebrequest" ]
aliases = [ "/questions/71747" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Different results when making a HttpWebRequest and when using Postman](/questions/71747/different-results-when-making-a-httpwebrequest-and-when-using-postman)

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
<span id="post-71747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71747-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I am trying to get Geo coordinates from a .NET Web App using HttpWebRequest and requesting this link: <a href="https://nominatim.openstreetmap.org/search?q=2+$+2A+Cyclone+Street+3995+WONTHAGGI&amp;country=au&amp;format=json&amp;addressdetails=1.">https://nominatim.openstreetmap.org/search?q=2+$+2A+Cyclone+Street+3995+WONTHAGGI&amp;country=au&amp;format=json&amp;addressdetails=1.</a> In my app, I receive 10 results but none of them are from Australia. If a request the same link from Postman, I receive one result from Australia. Why the difference? Should I set something specific in the web app? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postman" rel="tag" title="see questions tagged &#39;postman&#39;">postman</span> <span class="post-tag tag-link-httpwebrequest" rel="tag" title="see questions tagged &#39;httpwebrequest&#39;">httpwebrequest</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Nov '19, 11:56</strong></p>
<img src="https://secure.gravatar.com/avatar/46e3ecfb794cdbcba366fa931ee996f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raluca_A&#39;s gravatar image" />
<p><span>Raluca_A</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raluca_A has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71747" class="comments-container">
<span id="71773"></span>
<div id="comment-71773" class="comment">
<div id="post-71773-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Without the relevant code it is going to be very hard to help you with this. Are you escaping the URL properly in your app?</p>
</div>
<div id="comment-71773-info" class="comment-info">
<span class="comment-age">(22 Nov '19, 12:39)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="71832"></span>
<div id="comment-71832" class="comment">
<div id="post-71832-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Unrelated to your issue: Use &amp;countrycode=au, not &amp;country=au. &amp;country is part of the 'Alternative query string format' (<a href="http://nominatim.org/release-docs/latest/api/Search/)">http://nominatim.org/release-docs/latest/api/Search/)</a> and doesn't mix well if &amp;q is already set.</p>
</div>
<div id="comment-71832-info" class="comment-info">
<span class="comment-age">(26 Nov '19, 08:03)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="71935"></span>
<div id="comment-71935" class="comment">
<div id="post-71935-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I changed &amp;country to &amp;countrycode. Thanks.</p>
<p>I can paste here the code, sure, but it's something very simple:</p>
<p>string osmLink = "https://nominatim.openstreetmap.org/search?q=2+$+2A+Cyclone+Street+3995+WONTHAGGI&amp;country=au&amp;format=json&amp;addressdetails=1";</p>
<p>HttpWebRequest myRequest = (HttpWebRequest)WebRequest.Create(osmLink); myRequest.Method = "GET"; myRequest.UserAgent = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705;)";</p>
<p>WebResponse myResponse = myRequest.GetResponse();</p>
<p>string responseText = string.Empty; using (var reader = new StreamReader(myResponse.GetResponseStream(), System.Text.Encoding.UTF8)) { responseText = reader.ReadToEnd().Trim(); }</p>
</div>
<div id="comment-71935-info" class="comment-info">
<span class="comment-age">(02 Dec '19, 11:11)</span> <span class="comment-user userinfo">Raluca_A</span>
</div>
</div>
</div>
<div id="comment-tools-71747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71747-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

