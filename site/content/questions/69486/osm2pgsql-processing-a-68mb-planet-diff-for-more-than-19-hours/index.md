+++
type = "question"
title = "osm2pgsql processing a 68MB planet diff for more than 19 hours"
description = '''I installed Nominatim using full planet data from 2019-03-25 a couple of months ago, but initiated updates (as described at http://nominatim.org/release-docs/latest/admin/Import-and-Update/#updates) this week. Several diffs were applied at about 15-30 minutes per diff and then osm2pgsql got stuck on...'''
date = "2019-06-06T10:27:00Z"
lastmod = "2019-06-06T10:36:00Z"
weight = 69486
keywords = [ "planet", "diff", "nominatim", "osm2pgsql", "updates" ]
aliases = [ "/questions/69486" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [osm2pgsql processing a 68MB planet diff for more than 19 hours](/questions/69486/osm2pgsql-processing-a-68mb-planet-diff-for-more-than-19-hours)

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
<span id="post-69486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69486-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I installed Nominatim using full planet data from 2019-03-25 a couple of months ago, but initiated updates (as described at <a href="http://nominatim.org/release-docs/latest/admin/Import-and-Update/#updates">http://nominatim.org/release-docs/latest/admin/Import-and-Update/#updates</a>) this week. Several diffs were applied at about 15-30 minutes per diff and then osm2pgsql got stuck on a diff only 68MB large.</p>
<p>I interrupted <code>osm2pgsql</code> after about 6 hours and restarted it and it has been running at 100% CPU for almost 20 hours already.</p>
<p>During the first (interrupted) run its last output was</p>
<pre><code> Processing: Node(238k 1.9k/s) Way(31k 0.16k/s) Relation(700 16.67/s)</code></pre>
<p>while in the current run the count of processed relations is lower (570 vs 700)</p>
<pre><code> Processing: Node(238k 1.9k/s) Way(31k 0.16k/s) Relation(570 11.18/s)</code></pre>
<p>Note, however, that the first run was performed without any output redirection, while the output of the current run is redirected to a file which probably means that the most recent progress message is simply not flushed yet.</p>
<p>Having copied the update command as is, I didn't provide the <code>--osm2pgsql-cache</code> option, so it is using the default value of 2000MB. But the fact that <code>osm2pgsql</code> is running at 100% CPU doesn't suggest that the low cache setting can be the root cause of this problem.</p>
<p>Examining the stack trace at different times suggests that <code>osm2pgsql</code> is processing a complex relation and is busy with a deep recursion inside <code>osmium::area::detail::BasicAssembler::find_candidates()</code>:</p>
<pre><code>Using host libthread_db library &quot;/lib/x86_64-linux-gnu/libthread_db.so.1&quot;.
std::_Construct&lt;std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt;, std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt; &gt; (__p=&lt;optimized out&gt;) at /usr/include/c++/7/bits/stl_construct.h:75
75      { ::new(static_cast&lt;void*&gt;(__p)) _T1(std::forward&lt;_Args&gt;(__args)...); }
#0  std::_Construct&lt;std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt;, std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt; &gt; (__p=&lt;optimized out&gt;) at /usr/include/c++/7/bits/stl_construct.h:75
#1  std::__uninitialized_copy&lt;false&gt;::__uninit_copy&lt;std::move_iterator&lt;std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt;*&gt;, std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt;*&gt; (__result=&lt;optimized out&gt;, __last=..., 
    __first=...) at /usr/include/c++/7/bits/stl_uninitialized.h:83
#2  std::uninitialized_copy&lt;std::move_iterator&lt;std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt;*&gt;, std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt;*&gt; (__result=&lt;optimized out&gt;, __last=..., __first=...)
    at /usr/include/c++/7/bits/stl_uninitialized.h:134
#3  std::__uninitialized_copy_a&lt;std::move_iterator&lt;std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt;*&gt;, std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt;*, std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt; &gt; (
    __result=&lt;optimized out&gt;, __last=..., __first=...) at /usr/include/c++/7/bits/stl_uninitialized.h:289
#4  std::__uninitialized_move_if_noexcept_a&lt;std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt;*, std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt;*, std::allocator&lt;std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt; &gt; &gt; (__alloc=..., __result=&lt;optimized out&gt;, __last=0x55b024d324e0, __first=0x55b024d31d20)
    at /usr/include/c++/7/bits/stl_uninitialized.h:312
#5  std::vector&lt;std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt;, std::allocator&lt;std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt; &gt; &gt;::_M_realloc_insert&lt;osmium::area::detail::location_to_ring_map const&amp;, bool&gt; (
    this=this@entry=0x7ffd2f638998, __position=
  {first = {location = {m_x = 2000, m_y = 0, static undefined_coordinate = 2147483647}, ring_it = &lt;error reading variable: Cannot access memory at address 0xf91&gt;, start = 164}, second = 208}, __args#0=..., __args#1=@0x7ffd2f638980: true)
    at /usr/include/c++/7/bits/vector.tcc:424
#6  0x000055b01f0d28fe in std::vector&lt;std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt;, std::allocator&lt;std::pair&lt;osmium::area::detail::location_to_ring_map, bool&gt; &gt; &gt;::emplace_back&lt;osmium::area::detail::location_to_ring_map const&amp;, bool&gt; (this=this@entry=0x7ffd2f638998, __args#0=..., __args#1=@0x7ffd2f638980: true)
    at /usr/include/c++/7/bits/vector.tcc:105
#7  0x000055b01f0d5d66 in osmium::area::detail::BasicAssembler::find_candidates (this=this@entry=0x7ffd2f63c280, 
    candidates=std::vector of length 0, capacity 0, loc_done=std::unordered_set with 62 elements = {...}, 
    xrings=std::vector of length 672, capacity 672 = {...}, cand=...)
    at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/contrib/libosmium/osmium/area/detail/basic_assembler.hpp:736
&#10;... more osmium::area::detail::BasicAssembler::find_candidates() frames ...
....
... more osmium::area::detail::BasicAssembler::find_candidates() frames ...
&#10;#68 0x000055b01f0d5e04 in osmium::area::detail::BasicAssembler::find_candidates (this=this@entry=0x7ffd2f63c280, 
    candidates=std::vector of length 0, capacity 0, loc_done=std::unordered_set with 62 elements = {...}, 
    xrings=std::vector of length 672, capacity 672 = {...}, cand=...)
    at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/contrib/libosmium/osmium/area/detail/basic_assembler.hpp:750
#69 0x000055b01f0dae1d in osmium::area::detail::BasicAssembler::join_connected_rings (this=this@entry=0x7ffd2f63c280, 
    open_ring_its=std::__cxx11::list = {...})
    at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/contrib/libosmium/osmium/area/detail/basic_assembler.hpp:802
#70 0x000055b01f0dbcb4 in osmium::area::detail::BasicAssembler::create_rings_complex_case (
    this=this@entry=0x7ffd2f63c280)
    at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/contrib/libosmium/osmium/area/detail/basic_assembler.hpp:920
#71 0x000055b01f0dc842 in osmium::area::detail::BasicAssembler::create_rings (this=0x7ffd2f63c280)
    at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/contrib/libosmium/osmium/area/detail/basic_assembler.hpp:1087
#72 0x000055b01f0ce9b0 in osmium::area::GeomAssembler::operator() (out_buffer=..., ways_buffer=..., relation=..., 
    this=0x7ffd2f63c280) at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/contrib/libosmium/osmium/area/geom_assembler.hpp:112
#73 geom::osmium_builder_t::get_wkb_multipolygon[abi:cxx11](osmium::Relation const&amp;, osmium::memory::Buffer const&amp;) (
    this=0x55b02047cf98, rel=..., ways=...) at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/osmium-builder.cpp:159
#74 0x000055b01f0a9c3d in output_gazetteer_t::process_relation (this=0x55b02047ca30, rel=...)
    at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/output-gazetteer.cpp:704
#75 0x000055b01f05d080 in osmdata_t::relation_modify (this=&lt;optimized out&gt;, rel=...)
    at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/osmdata.cpp:129
#76 0x000055b01f06ee82 in parse_osmium_t::relation (this=this@entry=0x7ffd2f63cab0, rel=...)
    at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/parse-osmium.cpp:183
#77 0x000055b01f06fe70 in osmium::detail::apply_item_impl&lt;parse_osmium_t&amp;, osmium::memory::Item&gt; (handler=..., item=...)
    at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/contrib/libosmium/osmium/visitor.hpp:68
#78 osmium::apply_item&lt;osmium::memory::Item, parse_osmium_t&amp;&gt; (item=...)
    at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/contrib/libosmium/osmium/visitor.hpp:206
#79 osmium::apply&lt;osmium::io::InputIterator&lt;osmium::io::Reader, osmium::memory::Item&gt;, parse_osmium_t&amp;&gt; (end=..., it=...)
    at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/contrib/libosmium/osmium/visitor.hpp:220
#80 osmium::apply&lt;osmium::io::Reader, parse_osmium_t&amp;&gt; (c=...)
    at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/contrib/libosmium/osmium/visitor.hpp:229
#81 parse_osmium_t::stream_file (this=0x7ffd2f63cab0, filename=..., fmt=&quot;auto&quot;)
    at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/parse-osmium.cpp:128
#82 0x000055b01f04ff2d in main (argc=&lt;optimized out&gt;, argv=&lt;optimized out&gt;)
    at /srv/nominatim/Nominatim-3.2.0/osm2pgsql/osm2pgsql.cpp:86</code></pre>
<p>I wonder if anything is wrong with this run, or such anomalies are possible.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '19, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/99b789500bffcb3af64d88e4059f78d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leon%20Manukyan&#39;s gravatar image" />
<p><span>Leon Manukyan</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leon Manukyan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69486" class="comments-container">
&#10;</div>
<div id="comment-tools-69486" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69486-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="69487"></span>

<div id="answer-container-69487" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69487-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Leon Manukyan has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your issue is likely due to <a href="https://github.com/openstreetmap/osm2pgsql/issues/925">https://github.com/openstreetmap/osm2pgsql/issues/925</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '19, 10:36</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-69487" class="comments-container">
&#10;</div>
<div id="comment-tools-69487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69487-form-container" class="comment-form-container">
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

