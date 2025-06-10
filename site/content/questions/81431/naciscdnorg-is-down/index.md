+++
type = "question"
title = "naciscdn.org is down?"
description = '''I&#x27;m currently using a script which uses the CDN of NACIS. But for some reason their CDN is down and I&#x27;m getting the following error. Traceback (most recent call last):  File &quot;scripts/get-external-data.py&quot;, line 294, in &amp;lt;module&amp;gt;  main()  File &quot;scripts/get-external-data.py&quot;, line 230, in main  d...'''
date = "2021-08-24T09:52:00Z"
lastmod = "2021-09-20T15:23:00Z"
weight = 81431
keywords = [ "openstreetmap-carto", "osm-carto" ]
aliases = [ "/questions/81431" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [naciscdn.org is down?](/questions/81431/naciscdnorg-is-down)

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
<span id="post-81431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81431-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently using a <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/scripts/get-external-data.py">script</a> which uses the CDN of NACIS. But for some reason their CDN is down and I'm getting the following error.</p>
<pre><code>Traceback (most recent call last):
  File &quot;scripts/get-external-data.py&quot;, line 294, in &lt;module&gt;
    main()
  File &quot;scripts/get-external-data.py&quot;, line 230, in main
    download = s.get(source[&quot;url&quot;], headers=headers)
  File &quot;/usr/lib/python3/dist-packages/requests/sessions.py&quot;, line 533, in get
    return self.request(&#39;GET&#39;, url, **kwargs)
  File &quot;/usr/lib/python3/dist-packages/requests/sessions.py&quot;, line 520, in request
    resp = self.send(prep, **send_kwargs)
  File &quot;/usr/lib/python3/dist-packages/requests/sessions.py&quot;, line 630, in send
    r = adapter.send(request, **kwargs)
  File &quot;/usr/lib/python3/dist-packages/requests/adapters.py&quot;, line 508, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host=&#39;naciscdn.org&#39;, port=443): Max retries exceeded with url: /naturalearth/110m/cultural/ne_110m_admin_0_boundary_lines_land.zip (Caused by NewConnectionError(&#39;&lt;urllib3.connection.VerifiedHTTPSConnection object at 0x7f501cfe44e0&gt;: Failed to establish a new connection: [Errno 110] Connection timed out&#39;,))</code></pre>
<p>Does anyone have any idea why their CDN is down and when I could expect it to be available again?</p>
<p><strong><a href="https://downforeveryoneorjustme.com/naciscdn.org">Current status</a></strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap-carto" rel="tag" title="see questions tagged &#39;openstreetmap-carto&#39;">openstreetmap-carto</span> <span class="post-tag tag-link-osm-carto" rel="tag" title="see questions tagged &#39;osm-carto&#39;">osm-carto</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '21, 09:52</strong></p>
<img src="https://secure.gravatar.com/avatar/04175cc004ecad1e262fad8e94f86d62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KoenMlt&#39;s gravatar image" />
<p><span>KoenMlt</span><br />
<span class="score" title="42 reputation points">42</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KoenMlt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Aug '21, 10:52</strong> </span></p>
</div>
</div>
<div id="comments-container-81431" class="comments-container">
<span id="81433"></span>
<div id="comment-81433" class="comment">
<div id="post-81433-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes - there has been chat on their github about it. I'm sure they'll fix it.</p>
</div>
<div id="comment-81433-info" class="comment-info">
<span class="comment-age">(24 Aug '21, 09:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="81434"></span>
<div id="comment-81434" class="comment">
<div id="post-81434-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>, would you have a link to the conversation, please?</p>
</div>
<div id="comment-81434-info" class="comment-info">
<span class="comment-age">(24 Aug '21, 09:59)</span> <span class="comment-user userinfo">KoenMlt</span>
</div>
</div>
<span id="81435"></span>
<div id="comment-81435" class="comment">
<div id="post-81435-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://github.com/nvkelso/natural-earth-vector/issues/574#issuecomment-904313518">https://github.com/nvkelso/natural-earth-vector/issues/574#issuecomment-904313518</a> is where I saw it.</p>
<p>There have been issues in this area previously with the redirection between the main natural earth site and the CDN. See the links from <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/4249">https://github.com/gravitystorm/openstreetmap-carto/issues/4249</a> .</p>
</div>
<div id="comment-81435-info" class="comment-info">
<span class="comment-age">(24 Aug '21, 11:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="81824"></span>
<div id="comment-81824" class="comment">
<div id="post-81824-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>See gist at <a href="https://github.com/nvkelso/natural-earth-vector/issues/581#issuecomment-916250782">https://github.com/nvkelso/natural-earth-vector/issues/581#issuecomment-916250782</a></p>
</div>
<div id="comment-81824-info" class="comment-info">
<span class="comment-age">(20 Sep '21, 15:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-81431" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81431-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

