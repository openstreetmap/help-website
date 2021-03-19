+++
type = "question"
title = "Using tshark to save filtered packets to file"
description = '''Hello.  I want to use tshark with this display filter &quot;http.content_type contains html&quot; and save each resulting reassembled packets to their own separate file, not one file for all flows. Is that possible ? What I could come up with was  tshark -r test.packets -Y &quot;http.content_type contains html&quot; -w...'''
date = "2014-12-29T00:38:00Z"
lastmod = "2016-12-26T03:47:00Z"
weight = 38759
keywords = [ "multiple-files", "extract", "tshark" ]
aliases = [ "/questions/38759" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Using tshark to save filtered packets to file](/questions/38759/using-tshark-to-save-filtered-packets-to-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38759-score" class="post-score" title="current number of votes">1</div><span id="post-38759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello.</p><p>I want to use tshark with this display filter "http.content_type contains html" and save each resulting reassembled packets to their own separate file, not one file for all flows. Is that possible ?</p><p>What I could come up with was</p><pre><code>tshark -r test.packets -Y &quot;http.content_type contains html&quot; -w htmlfiles.packets</code></pre><p>But that's not even close to what was intended. This is the graphical way to do it in wireshark</p><p><img src="https://ychaouche.informatick.net/_media/wireshark.png?cache=" alt="wireshark version" /></p><p>Thanks for any help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-multiple-files" rel="tag" title="see questions tagged &#39;multiple-files&#39;">multiple-files</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '14, 00:38</strong></p><img src="https://secure.gravatar.com/avatar/94eb051be96f49a1665b097330fd97bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ychaouche&#39;s gravatar image" /><p><span>ychaouche</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ychaouche has one accepted answer">100%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Dec '16, 02:56</strong> </span></p></div></div><div id="comments-container-38759" class="comments-container"></div><div id="comment-tools-38759" class="comment-tools"></div><div class="clear"></div><div id="comment-38759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="40362"></span>

<div id="answer-container-40362" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40362-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40362-score" class="post-score" title="current number of votes">2</div><span id="post-40362-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ychaouche has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you looked at the built-in export option for HTTP (File -&gt; Export Objects -&gt; HTTP and then choose "Save All")?</p><p>If you only need "html" objects, first filter on the html content type, then "export specified packets to disk", load the newly saved file and then go to "Export Objects".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '15, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40362" class="comments-container"><span id="58335"></span><div id="comment-58335" class="comment"><div id="post-58335-score" class="comment-score"></div><div class="comment-text"><p>Exactly what I was looking for, no need for tshark ! thanks a ton sorry for late reply.</p></div><div id="comment-58335-info" class="comment-info"><span class="comment-age">(26 Dec '16, 03:47)</span> <span class="comment-user userinfo">ychaouche</span></div></div></div><div id="comment-tools-40362" class="comment-tools"></div><div class="clear"></div><div id="comment-40362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38799"></span>

<div id="answer-container-38799" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38799-score" class="post-score" title="current number of votes">1</div><span id="post-38799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would think there's some way to do that, but I can't seem to find it. For most fields you can get their value using the "<code>-T fields -e [fieldname]</code>" command switch for tshark, but in HTTP the field would be the <code>data-text-lines</code> field, but that will only give you something like "<code>Line-based text data: text/html</code>" instead of the whole content body.</p><p>So here's a way to do it using a Lua script - copy/paste the Lua script code at the bottom of this answer into a file, such as <code>extract.lua</code>. Then run tshark in the following way:</p><pre><code># the below is all one line
tshark -r [input_filename] -Y &#39;http.content_type contains html&#39; -X lua_script:extract.lua
    -X lua_script1:data-text-lines -T fields -e extractor.value.string &gt; output_file.txt</code></pre><p>What that will do is read in the file ("<code>[input_filename]</code>"), filter the packets so you only get the ones with content-type html, with the Lua script file named "<code>extract.lua</code>", and pass into the Lua script an argument of "<code>data-text-lines</code>" which the Lua script uses as the field you want to extract. The Lua script will create a new field called "<code>extractor.value.string</code>" of the string contents of the passed-in field "<code>data-text-lines</code>", so the "<code>-T fields -e extractor.value.string</code>" switch tells tshark to print that out. It then saves the output to a file using the "<code>&gt; output_file.txt</code>" .</p><p>Here's the Lua script:</p><hr /><pre><code>-- grab the passed-in argument(s)
local args = { ... }

-- exit if no arguments were passed in
if #args == 0 then
    return
end

-- a table to hold field extractors
local fields = {}

-- create field extractor(s) for the passed-in argument(s)
for i, arg in ipairs(args) do
    fields[i] = Field.new(arg)
end

-- our fake protocol
local exproto = Proto.new(&quot;extractor&quot;, &quot;Data Extractor&quot;)

-- the new fields that contain the extracted data (one in string form, one in hex)
local exfield_string = ProtoField.new(&quot;Extracted String Value&quot;, &quot;extractor.value.string&quot;, ftypes.STRING)
local exfield_hex    = ProtoField.new(&quot;Extracted Hex Value&quot;, &quot;extractor.value.hex&quot;, ftypes.STRING)

-- register the new fields into our fake protocol
exproto.fields = { exfield_string, exfield_hex }

function exproto.dissector(tvbuf,pktinfo,root)
    local tree = nil

    for i, field in ipairs(fields) do
        -- extract the field into a table of FieldInfos
        finfos = { field() }

        if #finfos &gt; 0 then
            -- add our proto if we haven&#39;t already
            if not tree then
                tree = root:add(exproto)
            end

            for _, finfo in ipairs(finfos) do
                -- get a TvbRange of the FieldInfo
                local ftvbr = finfo.tvb
                tree:add(exfield_string, ftvbr:string(ENC_UTF_8))
                tree:add(exfield_hex,tostring(ftvbr:bytes()))
            end
        end
    end

end

register_postdissector(exproto, true)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '14, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Dec '14, 10:31</strong> </span></p></div></div><div id="comments-container-38799" class="comments-container"><span id="40359"></span><div id="comment-40359" class="comment"><div id="post-40359-score" class="comment-score"></div><div class="comment-text"><p>How can I store the result for each matched packet to a separate file? Not just store all the content into one file. Thanks</p></div><div id="comment-40359-info" class="comment-info"><span class="comment-age">(07 Mar '15, 17:43)</span> <span class="comment-user userinfo">gunxueqiucjw</span></div></div></div><div id="comment-tools-38799" class="comment-tools"></div><div class="clear"></div><div id="comment-38799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40074"></span>

<div id="answer-container-40074" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40074-score" class="post-score" title="current number of votes">0</div><span id="post-40074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have the same issue although I have approached it from a different way. I perform a capture using tshark and within the wireshark dissector, I read the values I want to record, in my case raw and enumerated values using tvb_get_bits8 and similar calls in doc/README.dissectors, then output these values to a data file, in my case, a comma delimited file for later perusal.</p><p>So to read these values, I have to step thru the messages thru wireshark. I ensure I do not have duplicate values by maintaining a binary array of sequence numbers so redundant messages aren't output. All sorted by time.</p><p>I admit this is a roundabout way of doing this. It works, and it's easy, but it involves stepping thru a lot of message in wireshark to get my data file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '15, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/36420b7f93367a51a9cf13147feaa89a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srmafghan&#39;s gravatar image" /><p><span>srmafghan</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srmafghan has no accepted answers">0%</span></p></div></div><div id="comments-container-40074" class="comments-container"></div><div id="comment-tools-40074" class="comment-tools"></div><div class="clear"></div><div id="comment-40074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

