+++
type = "question"
title = "Overpass - 429 after one query"
description = '''So I have this code that runs through a loop for municipality codes for Denmark, there are about 98 municipalities, using Python. I take all the nodes, ways and relations that match some amenities I want (pub|bar|cafe|restaurant| etc.) and put them into a list. It is very important that I have the m...'''
date = "2019-02-21T12:49:00Z"
lastmod = "2019-02-21T14:40:00Z"
weight = 68089
keywords = [ "overpass", "http429" ]
aliases = [ "/questions/68089" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass - 429 after one query](/questions/68089/overpass-429-after-one-query)

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
<span id="post-68089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68089-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So I have this code that runs through a loop for municipality codes for Denmark, there are about 98 municipalities, using Python. I take all the nodes, ways and relations that match some amenities I want (pub|bar|cafe|restaurant| etc.) and put them into a list. It is very important that I have the municipality code for each amenity, and this is the only way I found out to make it work.</p>
<p>So I am doing 98 requests, I have had a sleep timer of 6 seconds, but now lately I am getting blocked even after just one request, even if I have a sleep timer of 10 seconds. Is there a way to rewrite this code so that I can do this in only one request perhaps, so that I dont get the 429 error? I send each request with my contact details (the mail was wrong I saw, but fixed now).</p>
<p>I have done a lot of requests earlier when testing the code, but then I have done it only for one municipality, checking if I am getting the result I want, and then retesting, but always a limited amount of requests.</p>
<pre><code>for mun in range(len(mun_code)):
            overpass_query = &quot;&quot;&quot;
            [out:json];
            area[&#39;ISO3166-1&#39; = &#39;DK&#39;][admin_level = 2] -&gt; .a ;
            area[&quot;ref&quot; = &quot;{0}&quot;][admin_level = 7] -&gt; .b ;
            out body qt;
            (
             node(area.a)(area.b)[&quot;amenity&quot; ~ &quot;{1}&quot;] ;
             way(area.a)(area.b)[&quot;amenity&quot; ~ &quot;{1}&quot;] ;
             rel(area.a)(area.b)[&quot;amenity&quot; ~ &quot;{1}&quot;] ;
            ) ;
            out {2} qt ;
            &quot;&quot;&quot;.format(mun_code[mun], amenities, out)
&#10;            response = requests.get(overpass_url, 
                                    params={&#39;data&#39;: overpass_query}, 
                                    headers = {
                                        &#39;User-Agent&#39;: user_agent,
                                        &#39;From&#39;: mail 
                                    })</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-http429" rel="tag" title="see questions tagged &#39;http429&#39;">http429</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Feb '19, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/d67e2c05633b6060bc8a5fe06a9cc5e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karl_NO&#39;s gravatar image" />
<p><span>Karl_NO</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karl_NO has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Feb '19, 14:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-68089" class="comments-container">
<span id="68096"></span>
<div id="comment-68096" class="comment">
<div id="post-68096-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you think about downloading whole Denmark and performing your queries offline? E.g. by using osmium-tool, there are also python bindings available!</p>
</div>
<div id="comment-68096-info" class="comment-info">
<span class="comment-age">(21 Feb '19, 14:40)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68089" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68089-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

