+++
type = "question"
title = "osmium to extract admin and education institutes"
description = '''Could you guys please help me on forming the osmium command to extract all the admin places and educational institutes? I mean all the extracts mentioned in Nominatim import-admin.style ( the below keys) and educational places. I came up with this one, but not sure if it includes wiki data and other...'''
date = "2022-11-01T12:51:00Z"
lastmod = "2022-11-02T12:05:00Z"
weight = 86048
keywords = [ "osmium" ]
aliases = [ "/questions/86048" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osmium to extract admin and education institutes](/questions/86048/osmium-to-extract-admin-and-education-institutes)

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
<span id="post-86048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86048-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Could you guys please help me on forming the osmium command to extract all the admin places and educational institutes? I mean all the extracts mentioned in Nominatim import-admin.style ( the below keys) and educational places.</p>
<p>I came up with this one, but not sure if it includes wiki data and other things mentioned in the import-admin.style, and also for boundary do we have to mention place?</p>
<p><strong>Command I came up with</strong></p>
<pre><code>osmium tags-filter planet.osm.pbf amenity=university,school,college,kindergarten place=*  boundary=administrative,postal_code,place,political   o place_edu.osm.pbf</code></pre>
<p><strong>import-admin.style</strong></p>
<pre><code>[
{   &quot;keys&quot; : [&quot;wikipedia&quot;, &quot;wikipedia:*&quot;, &quot;wikidata&quot;],
    &quot;values&quot; : {
        &quot;&quot; : &quot;extra&quot;
    }
},
{
    &quot;keys&quot; : [&quot;*:prefix&quot;, &quot;*:suffix&quot;, &quot;name:prefix:*&quot;, &quot;name:suffix:*&quot;,
              &quot;name:etymology&quot;, &quot;name:signed&quot;, &quot;name:botanical&quot;, &quot;*:wikidata&quot;,
              &quot;addr:street:name&quot;, &quot;addr:street:type&quot;],
    &quot;values&quot; : {
        &quot;&quot; : &quot;skip&quot;
    }
},
{
    &quot;keys&quot; : [&quot;ref&quot;, &quot;int_ref&quot;, &quot;nat_ref&quot;, &quot;reg_ref&quot;, &quot;loc_ref&quot;, &quot;old_ref&quot;,
              &quot;iata&quot;, &quot;icao&quot;, &quot;pcode&quot;, &quot;ISO3166-2&quot;],
    &quot;values&quot; : {
        &quot;&quot; : &quot;ref&quot;
    }
},
{
    &quot;keys&quot; : [&quot;name&quot;, &quot;name:*&quot;, &quot;int_name&quot;, &quot;int_name:*&quot;, &quot;nat_name&quot;, &quot;nat_name:*&quot;,
              &quot;reg_name&quot;, &quot;reg_name:*&quot;, &quot;loc_name&quot;, &quot;loc_name:*&quot;,
              &quot;old_name&quot;, &quot;old_name:*&quot;, &quot;alt_name&quot;, &quot;alt_name:*&quot;, &quot;alt_name_*&quot;,
              &quot;official_name&quot;, &quot;official_name:*&quot;, &quot;place_name&quot;, &quot;place_name:*&quot;,
              &quot;short_name&quot;, &quot;short_name:*&quot;, &quot;brand&quot;],
    &quot;values&quot; : {
        &quot;&quot; : &quot;name&quot;
    }
},
{
    &quot;keys&quot; : [&quot;landuse&quot;],
    &quot;values&quot; : {
        &quot;cemetry&quot; : &quot;skip&quot;,
        &quot;&quot; : &quot;fallback,with_name&quot;
    }
},
{
    &quot;keys&quot; : [&quot;boundary&quot;],
    &quot;values&quot; : {
        &quot;administrative&quot; : &quot;main&quot;
    }
},
{
    &quot;keys&quot; : [&quot;place&quot;],
    &quot;values&quot; : {
        &quot;&quot; : &quot;main&quot;
    }
},
{
    &quot;keys&quot; : [&quot;country_code&quot;, &quot;ISO3166-1&quot;, &quot;is_in:country_code&quot;, &quot;is_in:country&quot;,
              &quot;addr:country&quot;, &quot;addr:country_code&quot;],
    &quot;values&quot; : {
        &quot;&quot; : &quot;country&quot;
    }
},
{
    &quot;keys&quot; : [&quot;addr:*&quot;, &quot;is_in:*&quot;, &quot;tiger:county&quot;],
    &quot;values&quot; : {
        &quot;&quot; : &quot;address&quot;
    }
},
{
    &quot;keys&quot; : [&quot;postal_code&quot;, &quot;postcode&quot;, &quot;addr:postcode&quot;,
              &quot;tiger:zip_left&quot;, &quot;tiger:zip_right&quot;],
    &quot;values&quot; : {
        &quot;&quot; : &quot;postcode&quot;
    }
},
{
    &quot;keys&quot; : [&quot;capital&quot;],
    &quot;values&quot; : {
        &quot;&quot; : &quot;extra&quot;
    }
}
]</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Nov '22, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/038b5d0f92a84c822414ce263fa7dd68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chaitu1975&#39;s gravatar image" />
<p><span>Chaitu1975</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chaitu1975 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86048" class="comments-container">
<span id="86058"></span>
<div id="comment-86058" class="comment">
<div id="post-86058-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I am a bit confused by the Nominatim reference, I don't now anything about the details of Nominatim and why that's relevant to you. What's relevant to Osmium is only the list of tags you are interested in. And there is an error in your command line. The <code>place=*</code> doesn't do what you intend, it should just be <code>place</code>.</p>
</div>
<div id="comment-86058-info" class="comment-info">
<span class="comment-age">(02 Nov '22, 07:50)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="86061"></span>
<div id="comment-86061" class="comment">
<div id="post-86061-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, thank you for your response. Sorry for the confusion. I thought I can explain easily by referencing its import style for the keys that I want to extract. I am going to try this command and see "osmium tags-filter planet.osm.pbf place wikipedia wikipedia wikidata amenity=university,school,college,kindergarten boundary=administrative,postal_code,place,political o place_edu.osm.pbf"</p>
</div>
<div id="comment-86061-info" class="comment-info">
<span class="comment-age">(02 Nov '22, 12:05)</span> <span class="comment-user userinfo">Chaitu1975</span>
</div>
</div>
</div>
<div id="comment-tools-86048" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86048-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

