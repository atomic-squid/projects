<?xml version="1.0" encoding="UTF-8"?>
<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
    <xsl:output method="xml" doctype-public="XSLT-compat" omit-xml-declaration="yes" encoding="UTF-8" indent="yes" />
    
    <xsl:template match="/MediaContainer">
        <root>
            <xsl:for-each select="Video/Media/Part">
                <row>
                    <key><xsl:value-of select="../../@key"/></key>
                    <media_id><xsl:value-of select="../@id"/></media_id>
                    <part_id><xsl:value-of select="@id"/></part_id>
                    <media_dur><xsl:value-of select="../@duration"/></media_dur>
                    <part_dur><xsl:value-of select="@duration"/></part_dur>
                    <collection>
                        <xsl:for-each select="../../Collection">
                            <xsl:if test="position() > 1">, </xsl:if>
                            <xsl:value-of select="@tag"/>
                        </xsl:for-each>
                    </collection>
                    <title><xsl:value-of select="../../@title"/></title>
                    <rating><xsl:value-of select="../../@contentRating"/></rating>
                    <year><xsl:value-of select="../../@year"/></year>
                    <release><xsl:value-of select="../../@originallyAvailableAt"/></release>
                    <width><xsl:value-of select="../@width"/></width>
                    <height><xsl:value-of select="../@height"/></height>
                    <res><xsl:value-of select="../@videoResolution"/></res>
                    <aspect><xsl:value-of select="../@aspectRatio"/></aspect>
                    <container><xsl:value-of select="../@container"/></container>
                    <vid_codec><xsl:value-of select="../@videoCodec"/></vid_codec>
                    <vid_f_rate><xsl:value-of select="../@videoFrameRate"/></vid_f_rate>
                    <aud_coded><xsl:value-of select="../@audioCodec"/></aud_coded>
                    <aud_chan><xsl:value-of select="../@audioChannels"/></aud_chan>
                    <full_path><xsl:value-of select="@file"/></full_path>
                </row>
            </xsl:for-each>
        </root>
    </xsl:template>
    
</xsl:transform>