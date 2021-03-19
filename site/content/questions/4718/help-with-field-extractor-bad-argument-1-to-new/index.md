+++
type = "question"
title = "Help with field extractor - bad argument #1 to &#x27;new&#x27;"
description = '''Hi, I am new to lua and trying to create a tap to extract data from my dissector and do some basic stats. However I get the following error reported when I start wireshark... Lua: Error during loading: ...&#92;PortableWireshark_1.4.4&#92;App&#92;Wireshark&#92;foo_tap.lua:2:  bad argument #1 to &#x27;new&#x27; (Field_new: a f...'''
date = "2011-06-24T02:47:00Z"
lastmod = "2011-06-24T18:28:00Z"
weight = 4718
keywords = [ "listener", "lua", "dissector", "tap", "fields" ]
aliases = [ "/questions/4718" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Help with field extractor - bad argument \#1 to 'new'](/questions/4718/help-with-field-extractor-bad-argument-1-to-new)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4718-score" class="post-score" title="current number of votes">1</div><span id="post-4718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am new to lua and trying to create a tap to extract data from my dissector and do some basic stats. However I get the following error reported when I start wireshark...</p><pre><code>Lua: Error during loading:
...\PortableWireshark_1.4.4\App\Wireshark\foo_tap.lua:2: 
bad argument #1 to &#39;new&#39; (Field_new: a field with this name must exist)</code></pre><p>Here is my code...</p><p><strong>"init.lua"</strong></p><pre><code>dofile(&quot;foo_dissector.lua&quot;)
dofile(&quot;foo_tap.lua&quot;)</code></pre><p><strong>"foo_dissector.lua"</strong></p><pre><code>do
    local p_foo = Proto(&quot;foo&quot;, &quot;p_foo&quot;)
    function p_foo.init()
    end
    local f = p_foo.fields
    f.bar = ProtoField.uint8(&quot;p_foo.bar&quot;,&quot;Foo Bar&quot;, base.DEC)
    function p_foo.dissector(tvb, pinfo, tree)
         --doing my disection stuff here
    end
    local tcp_table = DissectorTable.get(&quot;tcp.port&quot;)
    tcp_table:add(9999, p_foo)
end</code></pre><p><strong>"foo_tap.lua"</strong></p><pre><code>do
    local foobar_extractor = Field.new(&quot;p_foo.bar&quot;)
    local function foo_tap()
        local foo_tap = Listener.new(nil,&quot;p_foo&quot;);
        local tw = TextWindow.new(&quot;FooBar Tap&quot;)
        local function remove()
            foo_tap:remove()
        end
        tw:set_atclose(remove)
        function foo_tap.packet(pinfo,tvb)
             --doing some measuring stuff here
        end
        function foo_tap.draw()
            --drawing some stuff here
        end
        function foo_tap.reset()
        end
    end  
    register_menu(&quot;FOOBAR&quot;, foo_tap, MENU_TOOLS_UNSORTED)
end</code></pre><p>I am using wireshark portable Version 1.4.4 (SVN Rev 36110 from /trunk-1.4) Running on Windows XP Service Pack 3, build 2600</p><p>I thought all the init.lua scripts will be run before packets are read, at the end of the dissector registration process. So i expected that so long as <code>foo_dissector.lua</code> was loaded before <code>foo_tap.lua</code> then field <code>p_foo.bar</code> exists and should be useable as a field extractor?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-listener" rel="tag" title="see questions tagged &#39;listener&#39;">listener</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '11, 02:47</strong></p><img src="https://secure.gravatar.com/avatar/e9a64b38c3c80a882aa3c808b71cccbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrb&#39;s gravatar image" /><p><span>mrb</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>24 Jun '11, 18:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4718" class="comments-container"></div><div id="comment-tools-4718" class="comment-tools"></div><div class="clear"></div><div id="comment-4718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4749"></span>

<div id="answer-container-4749" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4749-score" class="post-score" title="current number of votes">1</div><span id="post-4749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3513">bug</a> others have seen before. You should sign into Bugzilla to vote for its fix (I just did).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '11, 18:28</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-4749" class="comments-container"></div><div id="comment-tools-4749" class="comment-tools"></div><div class="clear"></div><div id="comment-4749-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

