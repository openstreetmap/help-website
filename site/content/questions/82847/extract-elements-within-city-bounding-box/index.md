+++
type = "question"
title = "Extract elements within city bounding box"
description = '''Given a city name, I&#x27;m trying to extract all nodes and ways that are located inside this city. But instead of a polygon shaped region, I want all elements inside the bounding box that surrounds this polygon shaped city region. I checked out Osmium-tool, but it only provides two functionalities:  tag...'''
date = "2021-12-16T10:32:00Z"
lastmod = "2021-12-20T09:33:00Z"
weight = 82847
keywords = [ "filter", "osmium" ]
aliases = [ "/questions/82847" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extract elements within city bounding box](/questions/82847/extract-elements-within-city-bounding-box)

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
<span id="post-82847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82847-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Given a city name, I'm trying to extract all nodes and ways that are located inside this city. But instead of a polygon shaped region, I want all elements inside the bounding box that surrounds this polygon shaped city region.</p>
<p>I checked out Osmium-tool, but it only provides two functionalities:</p>
<ul>
<li><code>tags-filter</code>: extract data filtered by tags (i.e. city name)</li>
<li><code>extract</code>: extract data given bounding box coordinates</li>
</ul>
<p>The first only returns the data inside the polygon shaped region and the second requires bounding box coordinates.</p>
<p>So is there a lib or a tool to extract that data or at least finds bounding box coordinates for a given city?</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '21, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/4404ad9bdd18f47ae5bd0f0551047e19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PoRouS&#39;s gravatar image" />
<p><span>PoRouS</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PoRouS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82847" class="comments-container">
&#10;</div>
<div id="comment-tools-82847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82847-form-container" class="comment-form-container">
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

<span id="82851"></span>

<div id="answer-container-82851" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82851-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Determining a bounding box for a polygon is kind of trivial. If you have the polygon in any kind of textual representation it should only take minutes in your favorite scripting language to determine the required values.</p>
<p>So the problem is more finding the polygon data for the specific city, in many countries you should be able to get that from OSM itself, in other places you might need to use 3rd party sources or simply draw a bounding box yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '21, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-82851" class="comments-container">
<span id="82854"></span>
<div id="comment-82854" class="comment">
<div id="post-82854-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>osmium fileinfo</code> will also give you the bounding box of an OSM file. So if you have a relation for your city, Osmium can help you.</p>
</div>
<div id="comment-82854-info" class="comment-info">
<span class="comment-age">(16 Dec '21, 18:55)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-82851" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82851-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82866"></span>

<div id="answer-container-82866" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82866-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you both for the very fast answers!</p>
<p><a href="https://help.openstreetmap.org/users/2053/simonpoole"></a><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a></a> Yes, given the coordinates of the polygon nodes would make it easy to calculate a bounding box. But osmium tags-filter just filters and extracts the nodes into a file, so I don't have direct access to the coordinates, only afterwards. I was hoping that there is a functionality that handles that for me.</p>
<p><a href="https://help.openstreetmap.org/users/112/jochen-topf"></a><a href="https://help.openstreetmap.org/users/112/jochen-topf">@Jochen Topf</a></a> If I filter the country map for the city relation, then the bounding box of the resulting OSM file still contains the values of the whole country and not that of the extracted relation.</p>
<p>So probably I can solve it that way:<br />
- use libosmium to filter the data for the relation of the city<br />
- extract all nodes of that relation<br />
- determine min and max longitude and latitude coordinates to determine city bounding box<br />
- use osmium-tool to extract the data within this bounding box</p>
<p>But unfortunately, I'm struggling to access the nodes of a relation in libosmium. I hope you can give me a hint.<br />
I'm trying to use the following handler for that, but I'm stuck here:</p>
<pre><code>class NamesHandler : public osmium::handler::Handler {
public:
static void relation(const osmium::Relation&amp; relation)
{
    osmium::TagsFilter filter { false };
    filter.add_rule(true, &quot;name&quot;, &quot;Friedrichshafen&quot;);
    if (!osmium::tags::match_any_of(relation.tags(), filter))
        return;
&#10;    for (const auto&amp; member : relation.members()) {
        const auto&amp; object = member.get_object();
        if (!object.is_compatible_to(osmium::item_type::node))
            continue;
&#10;        // TODO: convert osmium::OSMObject to osmium::Node to access the location function
    }
}
};
&#10;int main()
{
    NamesHandler names_handler;
    osmium::io::Reader reader { &quot;input.pbf&quot;, osmium::osm_entity_bits::relation };
    osmium::apply(reader, names_handler);</code></pre>
<p>}</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '21, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/4404ad9bdd18f47ae5bd0f0551047e19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PoRouS&#39;s gravatar image" />
<p><span>PoRouS</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PoRouS has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Dec '21, 12:37</strong> </span></p>
</div>
</div>
<div id="comments-container-82866" class="comments-container">
<span id="82867"></span>
<div id="comment-82867" class="comment">
<div id="post-82867-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can use <code>osmium getid -r</code> to get everything belonging to a relation out of an OSM file. You can use a link like <a href="https://www.openstreetmap.org/api/0.6/relation/65606/full">https://www.openstreetmap.org/api/0.6/relation/65606/full</a> (here for the London relation) to get that data from the API. There are so many different ways of doing these things depening on what exactly you want to do that this goes beyond what can be answered here in a simple way.</p>
</div>
<div id="comment-82867-info" class="comment-info">
<span class="comment-age">(17 Dec '21, 12:57)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="82878"></span>
<div id="comment-82878" class="comment">
<div id="post-82878-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again for the hint.</p>
<p>I found another way using libosmium to find the nodes for a specified relation. My code is based on this example: <a href="https://github.com/osmcode/libosmium/blob/master/examples/osmium_area_test.cpp">https://github.com/osmcode/libosmium/blob/master/examples/osmium_area_test.cpp</a></p>
<p>I adapted the area callback to the following to gather the bounding box:</p>
<pre><code>static void area(const osmium::Area&amp; area)
{
    double lonMin = 180;
    double lonMax = -180;
    double latMin = 90;
    double latMax = -90;
    for (auto oit = area.cbegin&lt;osmium::OuterRing&gt;(); oit != area.cend&lt;osmium::OuterRing&gt;(); ++oit) {
        const osmium::NodeRefList&amp; nodes = *oit;
        for (const auto&amp; node : nodes) {
            lonMin = std::min(lonMin, node.lon());
            lonMax = std::max(lonMax, node.lon());
            latMin = std::min(latMin, node.lat());
            latMax = std::max(latMax, node.lat());
        }
    }
&#10;    std::cout &lt;&lt; &quot;Bounding box:\n&quot;;
    std::cout &lt;&lt; &quot;(&quot; &lt;&lt; lonMin &lt;&lt; &quot;,&quot; &lt;&lt; latMin &lt;&lt; &quot;,&quot; &lt;&lt; lonMax &lt;&lt; &quot;,&quot; &lt;&lt; latMax &lt;&lt; &quot;)\n&quot;;
}</code></pre>
<p>For the germany map this query takes pretty long, so I reduced the map beforehand with osmium-tool by filtering out relations that I need:</p>
<pre><code>osmium tags-filter germany-latest.osm.pbf wr/boundary=administrative -o germany_filtered.pbf --overwrite</code></pre>
</div>
<div id="comment-82878-info" class="comment-info">
<span class="comment-age">(20 Dec '21, 09:33)</span> <span class="comment-user userinfo">PoRouS</span>
</div>
</div>
</div>
<div id="comment-tools-82866" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82866-form-container" class="comment-form-container">
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

